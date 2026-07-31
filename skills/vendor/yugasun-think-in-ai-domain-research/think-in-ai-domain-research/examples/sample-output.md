# Example: Complete Domain Onboarding Pack Output

This file shows a complete example of the default output format — the "Domain Onboarding Pack" — for a fictional domain: **E-commerce Order Fulfillment**.

---

# E-commerce Order Fulfillment 快速入门包

## 1. 研究目标

We are learning the order fulfillment domain in order to design an automated order routing system.

The immediate downstream artifact is: a requirements document with acceptance criteria and edge-case test plan.

## 2. Source Inventory

| Source | Type | What It Can Support | What It Cannot Support |
|--------|------|---------------------|----------------------|
| Fulfillment SOP (v3.2) | Methodology | Standard workflow, SLA definitions, escalation rules | Real-world exceptions |
| Order logs (last 90 days) | Evidence | Actual fulfillment patterns, failure modes | Root causes (need investigation) |
| Warehouse team interview | Evidence | Pain points, workaround practices | Official policy (may conflict with SOP) |

## 3. 业务/领域概念地图

```
Customer Order
    ├── Order Line Items
    │   ├── SKU → Inventory Location
    │   └── Quantity → Availability Check
    ├── Shipping Address → Zone → Carrier Assignment
    └── Payment Status → Fraud Check → Fulfillment Authorization
         │
         ▼
Fulfillment Center
    ├── Pick → Pack → Ship
    ├── Split Shipment (partial availability)
    └── Backorder (out of stock)
         │
         ▼
Delivery
    ├── Tracking → Customer Notification
    ├── Exception → Reroute / Return
    └── Proof of Delivery → Order Complete
```

## 4. 核心对象

| Object | Plain Meaning | Key Fields / Evidence | Common Misread |
|--------|--------------|----------------------|----------------|
| Order | Customer's purchase request | order_id, lines[], shipping_address, payment_status | Confusing order with shipment (one order can have multiple shipments) |
| Fulfillment Center (FC) | Warehouse that picks and ships | fc_id, zone, capacity, inventory[] | Assuming FC = inventory source (some items ship from vendor directly) |
| SKU | Stock Keeping Unit | sku_id, weight, dimensions, fragile_flag | Treating SKU as unique item (same SKU exists in multiple FCs) |
| Shipment | A package sent to customer | shipment_id, carrier, tracking, lines[] | Assuming 1 order = 1 shipment (split shipments are common) |
| Backorder | Item out of stock, awaiting replenishment | sku_id, expected_date, supplier | Treating backorder as cancellation (customer may still want it) |

## 5. 规则、方法论或流程

**Standard Fulfillment Flow:**

```
Order Received
  → Payment Verified [Rule: must pass fraud check within 2 hours]
  → Inventory Reserved [Rule: reserve at nearest FC to shipping address]
  → Pick List Generated [Rule: batch picks for efficiency, single picks for express]
  → Packed [Rule: fragile items require bubble wrap + "FRAGILE" label]
  → Carrier Assigned [Rule: cheapest carrier that meets SLA]
  → Shipped [Rule: tracking number within 1 hour of carrier pickup]
  → Delivered [Rule: proof of delivery required for orders >$100]
```

**SLA Definitions:**
- Standard: 5-7 business days
- Express: 2-3 business days
- Same-day: order by 11am, delivered by 9pm (metro areas only)

## 6. 案例对齐与可迁移模式

| Dimension | Case A: Holiday Rush | Case B: Fragile Electronics | Transferable Pattern |
|-----------|---------------------|----------------------------|---------------------|
| Capacity | FC at 95% capacity, delayed picks | Normal capacity | Capacity monitoring is critical |
| Split shipment | 3 of 5 items in stock → partial ship | Single item, in stock | Always check per-line availability |
| Carrier | Used backup carrier (SLA missed) | Standard carrier, no issues | Need fallback carrier logic |
| Exception | Address correction after ship | Delivery refused by customer | Post-ship exception handling needed |

## 7. 判断链 / 工作流

```
Evidence: Order with 5 line items
  → Check inventory per line at nearest FC
  → 3 available, 2 at distant FC
  → Business meaning: split shipment OR wait for consolidation
  → Judgment: if customer chose express, split; if standard, wait 48h for consolidation
  → Boundary: cannot determine customer preference without explicit choice at checkout
```

## 8. 关键指标、字段或术语解释

| Term | Meaning | Why It Matters |
|------|---------|---------------|
| Fill rate | % of orders shipped complete from single FC | High fill rate = fewer split shipments = lower cost |
| Pick rate | Items picked per hour per worker | Drives staffing and FC capacity planning |
| Zone skipping | Shipping directly to destination zone's local hub | Reduces transit time but requires volume threshold |
| Dead stock | Inventory with no sales in 90+ days | Ties up FC space, should be flagged for clearance |

## 9. 典型风险、失败模式和常见误读

| Risk | Example | Impact | Signal |
|------|---------|--------|--------|
| Overselling | Inventory shows available but reserved by another order | Customer complaint, cancellation | Reservation lag >5 seconds |
| Wrong FC assignment | Item shipped from distant FC despite local availability | Extra shipping cost, SLA miss | Geo-routing logic not updated |
| Carrier failure | Carrier pickup delayed by 24+ hours | SLA breach, customer escalation | No automated fallback trigger |
| **Common misread:** assuming "shipped" = "delivered" | Tracking shows shipped but carrier has delay | Customer expectation mismatch | Need delivery estimation, not just ship date |

## 10. 当前证据能推出什么

[Facts and inferences supported by materials]

- ✅ Split shipments are common (30% of multi-item orders in logs)
- ✅ Holiday capacity is the #1 cause of SLA breaches
- ✅ Fragile items require special handling (confirmed by both SOP and warehouse team)
- ✅ Same-day delivery is limited to metro areas (SOP confirms)

## 11. 当前证据不能推出什么

[Boundaries — what cannot be concluded]

- ❌ Cannot determine optimal consolidation wait time (needs A/B test data)
- ❌ Cannot compare carrier reliability (only 90 days of data, seasonal bias)
- ❌ Cannot confirm if warehouse team's "priority lane" workaround is officially sanctioned
- ❌ Cannot infer customer preference for split vs. consolidated (no survey data)

## 12. 需要专家或权威来源确认的问题

1. Is the 48-hour consolidation window an SLA commitment or a guideline?
2. When warehouse team uses the "priority lane," who authorizes it?
3. For zone skipping, what's the minimum volume threshold per zone?
4. What's the escalation path when a carrier fails pickup for >12 hours?
5. Should fragile items have a dedicated inventory pool or be handled at pick time?

## 13. 可转化的研发产物

| Domain Insight | Requirement | Acceptance/Test | Eval/Benchmark | Human Boundary |
|----------------|-------------|-----------------|----------------|----------------|
| Split shipment logic | Implement per-line availability check | Each line independently routed | Test with 1, 3, 5, 10 item orders | Consolidation preference: customer choice needed |
| Capacity monitoring | Real-time FC capacity dashboard | Alert at >90% capacity | Simulate load spike | Threshold: validated by ops team |
| Carrier fallback | Auto-switch carrier on pickup failure | Switch within 2 hours of missed pickup | Test with mock carrier failure | Approved carrier list: ops team owns |
| Fragile handling | Fragile flag triggers special packaging | Correct packaging 100% of time | Test with mixed fragile/non-fragile orders | Fragile criteria: product team defines |

---

> This example demonstrates the full 13-section Domain Onboarding Pack format. In practice, section depth varies by domain complexity and available materials.
