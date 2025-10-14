# House Agents - Usage Examples

Practical examples for using house agents in real-world scenarios.

## Table of Contents

- [Single Agent Usage](#single-agent-usage)
  - [House Research Examples](#house-research-examples)
  - [House MCP Examples](#house-mcp-examples)
  - [House Bash Examples](#house-bash-examples)
- [Multi-Agent Workflows](#multi-agent-workflows)
- [Common Patterns](#common-patterns)
- [Anti-Patterns](#anti-patterns)

---

## Single Agent Usage

### House Research Examples

#### Example 1: Finding Security Issues

**You:**
```
Use house-research to find all instances where we're using eval() or innerHTML
```

**House Research Agent Returns:**
```
## Search Results: Potentially Unsafe Code Patterns

### Summary
Found 3 instances of eval() and 7 instances of innerHTML across the codebase.
Most are in legacy code, 2 require immediate attention.

### Key Findings

**1. Direct eval() usage (HIGH RISK)**
- Location: `src/utils/parser.js:42`
- Details: `eval(userInput)` - evaluating unsanitized user input
- Relevance: Critical security vulnerability

**2. innerHTML with user data**
- Location: `src/components/UserProfile.js:89`
- Details: `element.innerHTML = userData.bio` - XSS risk
- Relevance: User-supplied content rendered without sanitization

[... condensed results ...]

### Recommended Actions
1. Replace eval() in parser.js with JSON.parse()
2. Use textContent or DOMPurify for innerHTML cases
3. Audit remaining instances in legacy code
```

**Your Next Message:**
```
Replace the eval() in parser.js with a safe alternative
```

---

#### Example 2: Finding API Endpoints

**You:**
```
Use house-research to find all Express route definitions in the backend
```

**House Research Agent Returns:**
```
## Search Results: Express Routes

### Summary
Found 23 route definitions across 5 files. 12 GET, 8 POST, 3 DELETE routes.

### Key Findings by File

**src/routes/auth.js**
- `POST /api/auth/login` (line 15)
- `POST /api/auth/register` (line 32)
- `POST /api/auth/logout` (line 48)

**src/routes/users.js**
- `GET /api/users` (line 10)
- `GET /api/users/:id` (line 25)
- `PUT /api/users/:id` (line 42)
- `DELETE /api/users/:id` (line 67)

[... more routes ...]

### Patterns Observed
- Auth routes lack rate limiting
- User routes missing input validation middleware
- No API versioning (consider /v1/ prefix)

### Recommended Actions
1. Add rate limiting to auth endpoints
2. Implement input validation middleware
3. Consider API versioning strategy
```

---

### House MCP Examples

#### Example 1: Configuring Stripe

**You:**
```
Use house-mcp to set up Stripe webhook handling for subscription events
```

**House MCP Agent Returns:**
```
## Configuration: Stripe Webhook Handler

### Summary
Express middleware for handling Stripe subscription webhooks with signature verification.

### Configuration

```javascript
const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);
const express = require('express');

const webhookRouter = express.Router();

webhookRouter.post(
  '/webhook',
  express.raw({ type: 'application/json' }),
  async (req, res) => {
    const sig = req.headers['stripe-signature'];

    let event;
    try {
      event = stripe.webhooks.constructEvent(
        req.body,
        sig,
        process.env.STRIPE_WEBHOOK_SECRET
      );
    } catch (err) {
      return res.status(400).send(`Webhook Error: ${err.message}`);
    }

    switch (event.type) {
      case 'customer.subscription.created':
        await handleSubscriptionCreated(event.data.object);
        break;
      case 'customer.subscription.updated':
        await handleSubscriptionUpdated(event.data.object);
        break;
      case 'customer.subscription.deleted':
        await handleSubscriptionCanceled(event.data.object);
        break;
      default:
        console.log(`Unhandled event type ${event.type}`);
    }

    res.json({ received: true });
  }
);
```

### Important Notes
- Use `express.raw()` not `express.json()` - signature verification requires raw body
- Get STRIPE_WEBHOOK_SECRET from Stripe Dashboard → Developers → Webhooks
- Test with Stripe CLI: `stripe listen --forward-to localhost:3000/webhook`
- Production URL must be HTTPS

### Next Steps
1. Add webhook endpoint to your Express app
2. Implement handler functions (handleSubscriptionCreated, etc)
3. Configure webhook URL in Stripe Dashboard
4. Test with Stripe CLI before deploying
```

---

#### Example 2: WordPress Contact Form 7

**You:**
```
Use house-mcp to configure Contact Form 7 with custom validation and email notifications
```

**House MCP Agent Returns:**
```
## Configuration: Contact Form 7 Custom Setup

### Summary
CF7 form with email validation, honeypot spam protection, and custom email template.

### Form Configuration

```
[text* your-name placeholder "Your Name"]
[email* your-email placeholder "Your Email"]
[tel your-phone placeholder "Phone (Optional)"]
[textarea* your-message placeholder "Your Message"]
[submit "Send Message"]
```

### Custom Validation (functions.php)

```php
add_filter('wpcf7_validate_email*', 'custom_email_validation', 20, 2);

function custom_email_validation($result, $tag) {
    $email = isset($_POST['your-email']) ? trim($_POST['your-email']) : '';

    // Block disposable email domains
    $blocked_domains = ['tempmail.com', '10minutemail.com', 'guerrillamail.com'];
    $domain = substr(strrchr($email, "@"), 1);

    if (in_array($domain, $blocked_domains)) {
        $result->invalidate($tag, "Please use a permanent email address.");
    }

    return $result;
}
```

### Email Template

In CF7 form settings → Mail tab:

**Subject:** `[your-name] sent a message from [_site_title]`

**Message Body:**
```
Name: [your-name]
Email: [your-email]
Phone: [your-phone]

Message:
[your-message]

---
Sent from: [_remote_ip]
Time: [_date] [_time]
```

### Important Notes
- Enable "Use HTML content type" for styled emails
- Set up SMTP plugin (WP Mail SMTP) for reliable delivery
- Add honeypot field to prevent bot submissions
- Test emails go to spam → check SPF/DKIM records

### Next Steps
1. Install Contact Form 7 plugin
2. Create new form with the markup above
3. Add validation code to theme's functions.php
4. Configure email template in form settings
5. Test submission and check spam folder
```

---

### House Bash Examples

#### Example 1: Running Tests

**You:**
```
Use house-bash to run the test suite and analyze any failures
```

**House Bash Agent Returns:**
```
## Execution Results: Test Suite

### Status
❌ Failed - 3 tests failing

### Summary
Ran 47 tests in 2.3s. 44 passed, 3 failed. All failures in auth module.

### Commands Executed
1. `npm test`

### Key Results
- Total tests: 47
- Passed: 44 (93.6%)
- Failed: 3 (6.4%)
- Duration: 2.3 seconds

### Errors Found

**Error 1: JWT Token Validation**
```
FAIL src/auth/jwt.test.js
  ● JWT verification › should reject expired tokens

  Expected expired token to be rejected, but was accepted

  at Object.<anonymous> (src/auth/jwt.test.js:45:7)
```
**Likely Cause**: JWT library not checking expiration or system clock issue
**Suggested Fix**:
1. Check if `jwt.verify()` has `ignoreExpiration: false` option
2. Verify system time is correct (`date` command)
3. Check if test tokens actually expired

**Error 2: Password Hashing**
```
FAIL src/auth/password.test.js
  ● Password hashing › should generate different hashes for same password

  Expected different hashes but got identical results

  at Object.<anonymous> (src/auth/password.test.js:23:7)
```
**Likely Cause**: Salt not being generated or reused across calls
**Suggested Fix**: Ensure bcrypt.hash() generates new salt each time

**Error 3: Login Rate Limiting**
```
FAIL src/auth/rateLimit.test.js
  ● Rate limiting › should block after 5 failed attempts

  Expected request to be blocked but got 200 response

  at Object.<anonymous> (src/auth/rateLimit.test.js:67:7)
```
**Likely Cause**: Rate limiter not properly configured or Redis not running
**Suggested Fix**: Check Redis connection and rate limiter middleware order

### Next Steps
1. Fix JWT expiration checking in auth/jwt.js
2. Review bcrypt salt generation in auth/password.js
3. Verify rate limiter configuration and Redis connection
4. Re-run tests after fixes
```

---

#### Example 2: Building and Analyzing Output

**You:**
```
Use house-bash to run the production build and check for issues
```

**House Bash Agent Returns:**
```
## Execution Results: Production Build

### Status
✅ Success with warnings

### Summary
Build completed in 12.3s. Bundle size increased 15% from last build. 3 warnings found.

### Commands Executed
1. `npm run build`

### Key Results
- Build time: 12.3 seconds
- Output directory: dist/
- Main bundle: 245.3 KB (gzipped: 87.2 KB)
- Vendor bundle: 156.8 KB (gzipped: 52.1 KB)
- Total size: 402.1 KB

### Warnings Found

**Warning 1: Large Bundle Size**
```
WARNING in asset size limit: The following asset(s) exceed the recommended size limit (244 KiB).
  main.js (245.3 KiB)
```
**Suggested Fix**: Consider code splitting or dynamic imports for large dependencies

**Warning 2: Deprecated API Usage**
```
WARNING in ./src/utils/api.js
Module Warning (from ./node_modules/eslint-loader/index.js):
  axios.get() 'transformResponse' option is deprecated
```
**Suggested Fix**: Update to axios v1.0+ API or remove deprecated options

**Warning 3: Source Map Size**
```
WARNING in source-map-loader
Failed to parse source map from 'node_modules/some-package/dist/file.js'
```
**Suggested Fix**: Non-critical - third-party package issue, safe to ignore

### Output Highlights
```
✓ Built in 12.3s
✓ 23 modules transformed
✓ Build artifacts written to dist/

Bundle Analysis:
├─ main.js (245.3 KB)
│  ├─ React (45 KB)
│  ├─ Chart.js (89 KB) ← largest contributor
│  └─ Application code (111.3 KB)
└─ vendor.js (156.8 KB)
```

### Next Steps
1. Consider lazy-loading Chart.js (used on only 2 pages)
2. Update axios to latest version to remove deprecated API warning
3. Monitor bundle size in CI (set threshold at 250 KB)
4. Deploy to staging for testing
```

---

## Multi-Agent Workflows

### Workflow 1: Refactoring Authentication System

**Step 1: Research Current Implementation**
```
Use house-research to find all authentication-related code
```

**Step 2: Implement Changes**
```
[You make changes based on research findings]
```

**Step 3: Run Tests**
```
Use house-bash to run the auth tests and check for regressions
```

---

### Workflow 2: Adding New API Integration

**Step 1: Configuration**
```
Use house-mcp to set up the SendGrid email API integration
```

**Step 2: Implementation**
```
[You implement the email sending functionality]
```

**Step 3: Testing**
```
Use house-bash to run integration tests for the email service
```

---

### Workflow 3: Codebase Audit

**Step 1: Find Issues**
```
Use house-research to find all console.log statements in production code
```

**Step 2: Remove Debug Code**
```
[You remove or replace console.logs]
```

**Step 3: Verify Changes**
```
Use house-bash to run linter and ensure no debug statements remain
```

---

## Common Patterns

### Pattern 1: Search → Fix → Test

Best for: Bug fixes, code cleanup

```
1. "Use house-research to find all instances of [problem]"
2. [Make fixes]
3. "Use house-bash to run tests and verify fixes"
```

### Pattern 2: Configure → Implement → Deploy

Best for: New features, integrations

```
1. "Use house-mcp to configure [tool/service]"
2. [Implement using the configuration]
3. "Use house-bash to build and deploy"
```

### Pattern 3: Audit → Research → Implement

Best for: Large refactors, security reviews

```
1. "Use house-research to analyze the [system/module]"
2. [Review findings and plan changes]
3. "Use house-research to find similar patterns in other files"
4. [Implement changes across codebase]
5. "Use house-bash to run full test suite"
```

---

## Anti-Patterns

### ❌ Don't: Use for Simple Tasks

**Bad:**
```
Use house-research to read the auth.js file
```

**Good:**
```
Read src/auth/auth.js
```

*Why:* Single file reads don't need a sub-agent

---

### ❌ Don't: Chain Too Many Agents

**Bad:**
```
Use house-research to find X, then use house-mcp to configure Y,
then use house-bash to test Z, then use house-research to verify...
```

**Good:**
```
Use house-research to find X
[Review results, make decisions]
Use house-bash to test the changes
```

*Why:* Too many agent calls add latency. Let main Claude coordinate.

---

### ❌ Don't: Over-Specify Agent Tasks

**Bad:**
```
Use house-research to search for the word "async" in files matching
*.js pattern in the src directory, excluding node_modules, and return
results grouped by file
```

**Good:**
```
Use house-research to find all async functions in src/
```

*Why:* Let the agent determine search strategy. They're experts.

---

### ❌ Don't: Use When You Need Full Context

**Bad:**
```
Use house-research to help me understand how the auth system works
```

**Good:**
```
Explain how the authentication system in src/auth/ works
```

*Why:* Main Claude is better for explanations and learning. House agents are for heavy operations.

---

## Tips for Best Results

1. **Be Specific About Goals**
   - ✅ "Find all React components with memory leaks"
   - ❌ "Find React stuff"

2. **Let Agents Finish Before Next Step**
   - Review agent results before making decisions
   - Don't chain 5 agents in one message

3. **Use the Right Agent**
   - Searching files? → house-research
   - Configuring tools? → house-mcp
   - Running commands? → house-bash

4. **Trust Agent Expertise**
   - They know which tools to use
   - They know how to condense results
   - Review their work, but don't micromanage

5. **Iterate When Needed**
   - If agent returns too much: "Focus on files modified in last month"
   - If agent returns too little: "Also check the test files"

---

## Getting Help

Having issues with house agents?

1. Check agent YAML files for tool permissions
2. Verify you're using the right agent for the task
3. Try being more specific in your request
4. Break complex tasks into smaller steps

Remember: House agents are specialized workers, not replacements for main Claude. Use them for heavy operations, let main Claude handle coordination and implementation.
