---
name: webhook-design
description: Build reliable webhooks — retry, sign, verify, and deliver events without data loss.
metadata:
  category: backend
  tags: [webhook, event, callback, integration]
---

# Webhook Design

## Delivery
- Send HTTP POST to the registered URL
- Include a JSON body with event type, id, timestamp, and data
- Use idempotency keys to handle duplicate deliveries
- Retry with exponential backoff (3-5 attempts, 1min/5min/15min/1h)
- Dead-letter queue after max retries

## Security
- Sign every payload with HMAC-SHA256 using a shared secret
- Include signature in the header: `X-Signature: sha256=<hex>`
- Provide a secret that consumers can use to verify
- Allow consumers to verify the signature before processing

## Payload Format
```json
{
  "event_id": "evt_abc123",
  "event_type": "order.created",
  "created_at": "2026-01-01T00:00:00Z",
  "data": {
    "order_id": "ord_456",
    "amount": 2999,
    "currency": "USD"
  }
}
```

## Consumer Expectations
- Webhook endpoints should respond quickly (<5s) — process async
- Respond with 2xx to acknowledge receipt
- Respond with 4xx/5xx to trigger a retry
- Be idempotent — processing the same webhook twice is safe
- Log all received webhooks for debugging
