# Sample: AI tool description

Illustration of section 7.3. The tool reads capacity. It does not change the cluster. Unknowns are `TBD`.

**Tool name:** read_cluster_capacity

**Purpose:** Return the measured capacity of one named cluster.

**Allowed callers:** TBD

**Allowed targets:** One cluster named in the input. The tool must not configure, delete, or scale that cluster. The tool must not configure, delete, or scale any other resource.

**Input schema:** Cluster name and cluster type. The schema document is TBD.

**Output schema:** TBD. The output must not report unknown capacity as zero.

**Read or write behavior:** Read.

**External side effects:** None. A second call does not configure, delete, or scale a resource. Confirm that claim for the implementation: TBD.

**Required approval:** not applicable. This tool does not configure, delete, or scale a resource. A tool that writes must name the approver. Tool availability is not permission to execute.

**Timeout:** TBD

**Retry behavior:** TBD. State whether a retry can run a second read.

**Idempotency conditions:** A repeated read does not configure, delete, or scale a resource. The implementation proof is TBD.

**Failure response:** The tool returns an error. It does not return a capacity of zero for a failed read.

**Audit requirements:** TBD

Rules: L02, L03, L12, L13 not applicable because the tool is not destructive. Prohibited equivalence: tool availability is not permission to execute.

Do not use this card as the model-serving description. Serving facts belong in [sample-model-serving.md](sample-model-serving.md).
