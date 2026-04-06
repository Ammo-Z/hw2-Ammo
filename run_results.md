# Final Evaluation Results (Advanced Prompt)

## Case: case_1_deep_tech_normal (Normal - High Jargon)
**Expected Output**: Extract 3 tasks: Supplier to adjust SMT profile, EE to update DFM, PM to track yield.

### Model Output:
*   **Task**: Run a split-lot Design of Experiment (DOE) on 50 Printed Circuit Board Assemblies (PCBAs) with the updated reflow oven temperature profile, extending the soak zone by 15 seconds.
    *   **DRI**: SMT Supplier
    *   **Deadline**: Tonight

*   **Task**: Update Design for Manufacturability (DFM) guidelines for the Design Validation Test (DVT) build based on X-ray results to prevent recurrence of tombstoning on 0201 bypass capacitors near the Power Management Integrated Circuit (PMIC).
    *   **DRI**: EE (Electrical Engineer)
    *   **Deadline**: After X-ray results are available tomorrow

*   **Task**: Track the overall yield impact in Jira.
    *   **DRI**: PM (Project Manager)
    *   **Deadline**: Ongoing
---
## Case: case_2_escalation_conditional (Complex Conditions)
**Expected Output**: Capture the conditional supply chain tasks and engineering redesign backup plan.

### Model Output:
*   **Task:** Request Purchase Order (PO) approval for the broker buy of the TI motor driver Integrated Circuit (IC).
    **DRI:** GSM (Supply Manager)
    **Deadline:** EOD (End of Day) today
*   **Task:** Provide new schematic and Gerber files for a Printed Circuit Board (PCB) revision to support an alternative Allegro motor driver (as a backup plan).
    **DRI:** EE (Electrical Engineer)
    **Deadline:** Friday
---
## Case: case_3_edge_noise (Edge Case - Noise & Tangents)
**Expected Output**: Filter out 90% of the transcript (Shenzhen travel, VPN, expense reports) to find the single NRE invoice task.

### Model Output:
*   **Task:** Submit the Non-Recurring Engineering (NRE) invoice for $3,000 for the extra 5-axis fixture to Finance.
    **DRI:** GSM
    **Deadline:** This afternoon
---
## Case: case_4_extreme_hallucination (Extreme Failure Risk)
**Expected Output**: Accurately capture the *final* partial tooling release (core/cavity only) and ignore the sarcasm and canceled CMF change.

### Model Output:
*   **Task**: Issue Purchase Order (PO) for the core and cavity components of the T0 injection molding tooling for the bottom casing.
    *   **DRI**: GSM
    *   **Deadline**: Today
*   **Task**: Finish the drop test simulation for the bottom casing.
    *   **DRI**: ME
    *   **Deadline**: Wednesday
---
## Case: case_5_negotiation (Conflict Resolution)
**Expected Output**: Extract tasks for sending golden/limit samples and signing the SIP document.

### Model Output:
- Task: Create and mail a set of physical limit samples (golden samples) for anodized aluminum covers, demonstrating an acceptable 0.2mm scratch limit on the cosmetic A-surface.
    - DRI: Quality Engineer (QE)
    - Deadline: By Thursday (for mailing)
- Task: Sign the updated Standard Inspection Procedure (SIP), incorporating the new 0.2mm scratch limit. This task is contingent upon receiving and agreeing to the golden samples.
    - DRI: Supplier
    - Deadline: By next Monday (after receiving samples)
---
