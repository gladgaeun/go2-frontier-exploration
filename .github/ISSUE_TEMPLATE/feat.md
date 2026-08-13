---
name: Feat
about: Describe this issue template's purpose here.
title: ''
labels: ''
assignees: ''

---

## Feature Overview
* **Feature Title:** <!-- Name of the feature or algorithm improvement (e.g., Add Voronoi-based Frontier Weighting) -->
* **Target Modules:** <!-- Affected ROS 2 nodes, packages, or launch files (e.g., classical_frontier_detector, nav2.yaml) -->

---
## Feature Specifications

### Functional Requirements
- [ ] **Requirement 1:** <!-- High-level capability (e.g., Compute obstacle distance transform for each candidate frontier) -->
- [ ] **Requirement 2:** <!-- High-level capability (e.g., Expose dynamic weight parameter via ROS 2 launch file) -->

### ROS 2 Interface Changes (Optional)
* **New/Modified Topics:** <!-- e.g., Publish /f_scores (std_msgs/msg/Float32MultiArray) -->
* **New Parameters:** <!-- e.g., region_size_thresh (int), voronoi_weight (double) -->

---

## Task List

### Planned Tasks
- [ ] **Task 1: Architecture & Parameter Design**
  - [ ] <!-- Sub-task detail (e.g., Add 'voronoi_weight' parameter to launch script and C++ node) -->
- [ ] **Task 2: Code Implementation**
  - [ ] <!-- Sub-task detail (e.g., Implement OpenCV distance transform calculation in C++ node) -->
  - [ ] <!-- Sub-task detail (e.g., Update score calculation formula in publishFrontiers()) -->
- [ ] **Task 3: Integration & Testing**
  - [ ] <!-- Sub-task detail (e.g., Verify visualization markers in RViz2) -->
  - [ ] <!-- Sub-task detail (e.g., Conduct real-robot exploration benchmark on Go2) -->

### Implementation Details
```cpp
// Draft snippet of proposed function signatures, class methods, or logic flow
