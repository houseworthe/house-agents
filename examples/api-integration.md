# API Integration Example

## Scenario

You need to integrate Stripe payment processing into your application:
- Set up webhook handling
- Create subscription management
- Handle payment events

Without house agents, this involves reading 100+ pages of Stripe docs, which would fill your context.

## Step 1: Get Webhook Configuration

**Your prompt:**
```
Use house-mcp to set up Stripe webhook handling for subscription events (created, updated, canceled)
```

**Expected output:**
```markdown
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
    }

    res.json({ received: true });
  }
);
```

### Important Notes
- Use express.raw() NOT express.json() for signature verification
- Get STRIPE_WEBHOOK_SECRET from Stripe Dashboard
- Test with Stripe CLI: `stripe listen --forward-to localhost:3000/webhook`
- Production URL must be HTTPS

### Next Steps
1. Add webhook endpoint to Express app
2. Implement handler functions
3. Configure webhook URL in Stripe Dashboard
```

## Step 2: Implement the Configuration

Now work with main Claude to add this to your app:

```
Create src/webhooks/stripe.js with the webhook handler from house-mcp. Then implement the three handler functions for subscription events.
```

*Main Claude creates the file and implements handlers*

## Step 3: Create Subscription Management

**Your prompt:**
```
Use house-mcp to show me how to create and manage Stripe subscriptions (create, cancel, update payment method)
```

**Expected output:**
```markdown
## Configuration: Stripe Subscription Management

### Summary
Functions for creating, canceling, and managing Stripe subscriptions.

### Create Subscription

```javascript
async function createSubscription(customerId, priceId) {
  try {
    const subscription = await stripe.subscriptions.create({
      customer: customerId,
      items: [{ price: priceId }],
      payment_behavior: 'default_incomplete',
      payment_settings: { save_default_payment_method: 'on_subscription' },
      expand: ['latest_invoice.payment_intent'],
    });

    return {
      subscriptionId: subscription.id,
      clientSecret: subscription.latest_invoice.payment_intent.client_secret,
    };
  } catch (error) {
    throw new Error(`Subscription creation failed: ${error.message}`);
  }
}
```

### Cancel Subscription

```javascript
async function cancelSubscription(subscriptionId) {
  const subscription = await stripe.subscriptions.cancel(subscriptionId);
  return subscription;
}
```

### Important Notes
- Use `payment_behavior: 'default_incomplete'` for 3D Secure support
- Always expand payment_intent to get client_secret
- Handle errors for failed payments
- Consider grace periods for cancellation

### Next Steps
1. Create subscription management service
2. Add routes for create/cancel/update
3. Integrate with your user model
4. Test with Stripe test cards
```

## Step 4: Test the Integration

**Your prompt:**
```
Use house-bash to run the Stripe integration tests
```

**Expected output:**
```markdown
## Execution Results: Stripe Integration Tests

### Status
✅ Success

### Summary
All 12 Stripe integration tests passed in 4.3s.

### Key Results
- Webhook signature verification: ✓
- Subscription creation: ✓
- Subscription updates: ✓
- Subscription cancellation: ✓
- Error handling: ✓

### Next Steps
1. Configure webhook URL in Stripe Dashboard
2. Test with real webhook events using Stripe CLI
3. Deploy to staging environment
```

## Step 5: Verify Webhook Events

Test with Stripe CLI:

```
Use house-bash to run 'stripe listen --forward-to localhost:3000/webhook' and trigger a test event
```

## Complete Workflow Summary

| Step | Agent | Tokens | Time |
|------|-------|--------|------|
| Get webhook config | house-mcp | 3k | 20 sec |
| Implement handlers | main Claude | 8k | 1 min |
| Get subscription API | house-mcp | 3k | 20 sec |
| Implement service | main Claude | 10k | 2 min |
| Run tests | house-bash | 4k | 30 sec |
| **Total** | **Mixed** | **28k** | **~5 min** |

**Without agents:** 180k+ tokens, 15+ min (reading full Stripe docs)

## Why This Works

1. **house-mcp** digests verbose Stripe documentation
2. Returns only the working code you need
3. Main Claude implements without doc clutter
4. **house-bash** verifies everything works
5. Your context stays clean and focused

## Tips

- Use house-mcp for any complex API integration
- Request specific scenarios (webhooks, subscriptions, etc)
- Implement the config before requesting more
- Test incrementally with house-bash
- Keep API documentation out of main context

## Real Token Savings

Reading Stripe docs yourself:
- Webhook docs: ~45k tokens
- Subscription API docs: ~60k tokens
- Error handling docs: ~35k tokens
- Testing docs: ~40k tokens
- **Total: 180k tokens**

Using house-mcp:
- Webhook config: 3k tokens
- Subscription config: 3k tokens
- Testing summary: 4k tokens
- **Total: 10k tokens**

**Savings: 94%** 🎉
