# Incident Report: #001 - Order Payment Mismatch

## 🚨 Symptom

The customer completed the payment process, and the transaction was processed successfully. However, the order is not visible in the user interface, and no order confirmation was generated.

## 🔍 Root Cause Analysis (RCA)

- Investigated the database using a `LEFT JOIN` between `payments` and `orders` where `orders.order_id IS NULL`.
- Discovered an orphaned payment record with an invalid reference: `order_id = 999`, which does not exist in the `orders` table.

## 🛠️ Resolution (Data Fix)

Executed a targeted SQL update to sync the payment record with the correct order ID:

```sql
UPDATE payments SET order_id = 5 WHERE order_id = 999;
```
