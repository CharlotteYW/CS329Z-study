# Week 2 References

Current topic: Lecture 3, Retrieval-Augmented Generation. Lecture 2 review material is retained below. See the [Lecture 3 materials](../../resources/course-materials.md#l03) and [questions and answers](questions-and-answers.md).

The learner reported finishing the L03 video on November 23 and provided a short reflection. The [learner reflection and AI reference summary](questions-and-answers.md#lecture-3-reflection-and-reference-summary) are recorded. Retain the resources below for review; the next viewing resource is [Lecture 4](../week-03/references.md).

## Optional reading and comparison

- **Lecture 3 review, about 5–10 minutes.** Start with slides 16–19, then compare the hybrid search and reranking diagrams on PDF pages 49–50. Follow what a retriever returns and what a generator consumes. This supports the learner's current question. [Lecture 3 slides](https://web.stanford.edu/class/cs329z/slides/lecture03.pdf#page=16)
- **Contextual retrieval review, about 5–10 minutes, optional.** Read the contextual preprocessing example in Anthropic's article and the [worked Elasticsearch Q&A](questions-and-answers.md#how-does-contextual-retrieval-work-with-elasticsearch-chunks-and-indexes). Follow how added context enters both `search_text` and the embedding input. [Contextual retrieval](https://www.anthropic.com/research/contextual-retrieval)
- **Review (about 5–10 minutes).** Read Table 1 and the opening paragraphs of Section 4 of the Transformer paper. Compare the total work and sequential operations needed to process an input sequence. Then use the cache explanation to see why one cached decode step has a different cost. The [worked comparison](questions-and-answers.md#how-do-self-attention-and-recurrence-predict-the-next-token) covers both phases. [Transformer paper, Section 4](https://arxiv.org/html/1706.03762#S4) · [KV cache explanation](https://huggingface.co/docs/transformers/en/cache_explanation)
- **Optional derivation.** Equations 3–6 show how the query can be factored out of the weighted sum, and Equations 18–20 show the causal state update. See the [worked derivation](questions-and-answers.md#why-is-standard-softmax-attention-quadratic-and-linear-attention-linear). [Linear attention paper](https://arxiv.org/html/2006.16236)

## Sources for review

- Vaswani et al. explain scaled dot-product attention and compare the complexity and sequential dependencies of self-attention and recurrent layers. This is a Lecture 2 reading. [Attention Is All You Need](https://arxiv.org/html/1706.03762)
- Hugging Face's Transformers documentation shows how the query for a new token uses stored keys and values, and how the work and cache size change with context length. [How caching works](https://huggingface.co/docs/transformers/en/cache_explanation)
- Katharopoulos et al. factor the attention computation using a kernel feature map in Section 3.2 and derive a recurrent form of causal linear attention in Section 3.4. This is a Lecture 2 reading. [Transformers are RNNs](https://arxiv.org/html/2006.16236)

## Context windows and serving

- Meta describes its positional encoding in Section 3.2 and the staged increase from 8K to 128K during long-context pre-training in Section 3.4.2. [The Llama 3 Herd of Models](https://arxiv.org/html/2407.21783)
- vLLM documents `--max-model-len` as the combined prompt and output limit and explains how it can select a supported length within the available GPU memory. [vLLM engine arguments](https://docs.vllm.ai/en/stable/configuration/engine_args/#--max-model-len)

## Long-context evaluation

- Hsieh et al. evaluate retrieval, multi-hop tracing, and aggregation as input length grows. The benchmark illustrates the difference between supported input length and reliable performance on a task. [RULER](https://arxiv.org/abs/2404.06654)

## Pretraining and midtraining

- Hugging Face explains causal language modeling and how to form next-token targets from the same input sequence. [Causal language modeling](https://huggingface.co/docs/transformers/en/tasks/language_modeling)
- Team Olmo describes the decoder-only Transformer in Section 3.2, a broad pretraining mix in Section 3.4, and a targeted continuation mix in Section 3.5. Section 3.5.4 discusses tradeoffs when putting more weight on a particular domain. [Olmo 3 technical report](https://arxiv.org/html/2512.13961)

## Post-training and instruction tuning

- Section 4 of the Olmo 3 report describes the Think pipeline and the datasets for supervised fine-tuning, direct preference optimization, and reinforcement learning with verifiable rewards. [Olmo 3 technical report](https://arxiv.org/html/2512.13961)
- Hugging Face TRL documents chat formatting, label shifting, and how to apply loss only to completion or assistant tokens in supervised fine-tuning. [SFT Trainer documentation](https://huggingface.co/docs/trl/en/sft_trainer)

## Human feedback

- Ouyang et al. describe human demonstrations, comparison labels, reward model training, and PPO in Section 3.1 and Figure 2. [InstructGPT paper](https://arxiv.org/html/2203.02155)
- Rafailov et al. derive a method to fine-tune a model from preference pairs without fitting a separate reward model. [Direct Preference Optimization](https://arxiv.org/abs/2305.18290)

## Agent-specific training

- Section 5.2.1 describes how Ai2 collected tool-calling trajectories using real tool environments and a simulated environment. The scholarly search example in this week's Q&A is a simplified illustration. [Olmo 3 technical report](https://arxiv.org/html/2512.13961)
- Jin et al. train a model to issue search queries and condition on retrieved results over multiple steps, using an answer correctness reward. [Search-R1](https://arxiv.org/html/2503.09516)
- The original ReAct paper provides the title and author metadata used in the worked trajectory. [ReAct](https://arxiv.org/abs/2210.03629)

## SWE-smith and SWE-bench

- SWE-smith builds verifiable software engineering tasks and uses successful agent runs for supervised fine-tuning. This is an optional preview of the official reading for [Lecture 12](../../resources/course-materials.md#l12). [SWE-smith paper](https://arxiv.org/html/2504.21798) · [Project](https://swesmith.com/)
- SWE-bench collects real GitHub issues and uses repository tests to evaluate patches. [SWE-bench paper](https://arxiv.org/abs/2310.06770)
- The starting and fine-tuned checkpoints both identify `Qwen2ForCausalLM` as the architecture. The resulting model card describes the fine-tuning data and SWE-agent integration. [Qwen2.5-Coder-32B-Instruct configuration](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct/blob/main/config.json) · [SWE-agent-LM-32B configuration](https://huggingface.co/SWE-bench/SWE-agent-LM-32B/blob/main/config.json) · [SWE-agent-LM-32B model card](https://huggingface.co/SWE-bench/SWE-agent-LM-32B)

## Inference and serving

- The Lecture 2 slides introduce prefill and decode in the inference section and return to both phases after introducing the KV cache. [Lecture 2 slides, PDF page 120](https://web.stanford.edu/class/cs329z/slides/lecture02.pdf#page=120) · [PDF page 134](https://web.stanford.edu/class/cs329z/slides/lecture02.pdf#page=134)
- Sections 1 and 2 describe how prefill produces the first output token and decode generates subsequent tokens, and define time to first token and time per output token. [DistServe](https://arxiv.org/html/2401.09670v3)
- The attention matrices section shows how the newest query uses previous keys and values and how the KV cache grows during generation. [Transformers cache explanation](https://huggingface.co/docs/transformers/en/cache_explanation)
- vLLM documents how automatic prefix caching reuses matching prompt prefixes across requests, including later turns in a chat. [Automatic prefix caching](https://docs.vllm.ai/en/stable/features/automatic_prefix_caching/)

## Speculative decoding

- The lecture illustrates draft and target model cooperation and notes that draft accuracy can vary by domain. [Lecture 2 slides, PDF pages 136–137](https://web.stanford.edu/class/cs329z/slides/lecture02.pdf#page=136)
- Leviathan et al. give the verification algorithm and analyze when fewer sequential target passes reduce latency. Chen et al., cited in the lecture, describe parallel scoring of draft continuations and the sampling rule that preserves the target distribution. [Fast Inference from Transformers via Speculative Decoding](https://proceedings.mlr.press/v202/leviathan23a.html) · [Accelerating Large Language Model Decoding with Speculative Sampling](https://arxiv.org/abs/2302.01318)

## Inference-time scaling

- The lecture introduces test-time scaling and covers longer reasoning, repeated sampling, and self-consistency. [Lecture 2 slides, PDF pages 138–148](https://web.stanford.edu/class/cs329z/slides/lecture02.pdf#page=138)
- Lecture 2 pairs repeated sampling with Brown et al.'s study of candidate coverage and the ability of verifiers to select correct answers. [Lecture 2 slides, PDF pages 145–146](https://web.stanford.edu/class/cs329z/slides/lecture02.pdf#page=145) · [Large Language Monkeys](https://arxiv.org/html/2407.21787)
- Wang et al. sample diverse reasoning paths and aggregate their final answers. [Self-Consistency Improves Chain of Thought Reasoning in Language Models](https://arxiv.org/abs/2203.11171)
- Lecture 2 uses Inkling to illustrate how a per-token training cost can teach a model to respond to different effort settings. Thinking Machines Lab describes effort conditioning and the per-token cost in its release and documents the inference control separately. [Lecture 2 slides, PDF page 144](https://web.stanford.edu/class/cs329z/slides/lecture02.pdf#page=144) · [Inkling release and training description](https://thinkingmachines.ai/news/introducing-inkling/) · [Thinking effort documentation](https://tinker-docs.thinkingmachines.ai/cookbook/inkling/thinking-effort/)

## Structured I/O and constrained decoding

- Lecture 2 introduces constrained decoding and describes SGLang's use of finite state machines. The adjacent DSPy example supplies the intent labels used in the Q&A. [Lecture 2 slides, PDF pages 153–156](https://web.stanford.edu/class/cs329z/slides/lecture02.pdf#page=153) · [SGLang paper](https://arxiv.org/abs/2312.07104)
- Section 2 and Figure 2 of the XGrammar paper show grammar-guided generation with a per-token mask. [XGrammar paper](https://arxiv.org/html/2411.15100)
- The vLLM serving documentation shows how to supply a JSON Schema through the structured outputs configuration. [vLLM structured outputs documentation](https://docs.vllm.ai/en/stable/features/structured_outputs/)

## System One models

- Lecture 2 introduces classifiers with adaptable options for decisions and points to Contrastive Language Models. The linked project page was unavailable through the web reader. The authors' repository and model card describe the state and action encoders, contrastive training, and direct scoring. [Lecture 2 slides, PDF page 158](https://web.stanford.edu/class/cs329z/slides/lecture02.pdf#page=158) · [CLM repository](https://github.com/Contrastive-LM/CLM) · [CLM-8B model card](https://huggingface.co/Contrastive-LM/CLM-v0.1-8B)

## Avoiding context bloat

- Lecture 2 illustrates focused tool sets with Pi and recommends retrieving relevant memories and files. [Lecture 2 slides, PDF pages 166–167](https://web.stanford.edu/class/cs329z/slides/lecture02.pdf#page=166) · [Pi coding agent documentation](https://upd.dev/badlogic/pi-mono/src/commit/3559a43ba026be095e95483ef62012cee9e34e40/packages/coding-agent)
- The official course reading discusses focused tool sets, high-signal context, and just-in-time retrieval. [Effective Context Engineering for AI Agents](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents)

## Prefix reuse in agent context

- Lecture 2 illustrates how appending tokens preserves the existing prefix and how inserting tokens earlier changes later positions. [Lecture 2 slides, PDF pages 168–169](https://web.stanford.edu/class/cs329z/slides/lecture02.pdf#page=168)
- vLLM describes prefix matching with full token blocks and parent hashes, including how retained blocks are reused across requests. [vLLM prefix caching design](https://docs.vllm.ai/en/stable/design/prefix_caching/)

## Recursive language models

- Lecture 2 introduces RLMs in the context engineering section. The paper describes storing the input in a Python environment and making language model subcalls to inspect or transform parts of it. Its OOLONG experiments cover tasks that require aggregating information across a long input. [Lecture 2 slides, PDF pages 172–173](https://web.stanford.edu/class/cs329z/slides/lecture02.pdf#page=172) · [Recursive Language Models paper](https://arxiv.org/html/2512.24601) · [Author's illustrated introduction](https://alexzhang13.github.io/blog/2025/rlm/)

## Tool execution and file errors

- Python documents the file or directory lookup error and explains why attempting an operation and handling an exception can be preferable to a separate preflight check. These sources support the worked file-reading example in the L02 reflection. [FileNotFoundError](https://docs.python.org/3/library/exceptions.html#FileNotFoundError) · [File access and exception handling](https://docs.python.org/3/library/os.html#os.access)

## RAG pipeline

- Lecture 3 introduces the retriever and generator on PDF pages 16–19, indexing and chunking from page 23, and retrieval inside an agent loop on page 56. [Lecture 3 slides](https://web.stanford.edu/class/cs329z/slides/lecture03.pdf#page=16)
- Lewis et al. introduce retrieval-augmented generation with a dense retriever and a sequence-to-sequence generator. This is an official Lecture 3 reading. [Original RAG paper](https://arxiv.org/abs/2005.11401)
- Anthropic describes indexing chunks for embedding and BM25 retrieval, enriching chunks with document context, and reranking results. [Contextual retrieval](https://www.anthropic.com/research/contextual-retrieval)

## RAG engineering practice

- Elastic documents combining full-text and vector search through reciprocal rank fusion. [Hybrid search](https://www.elastic.co/docs/solutions/search/hybrid-search)
- Azure describes query planning, parallel subqueries, reranking, and source references in an agentic retrieval pipeline. Checked on November 19, 2026. [Agentic retrieval overview](https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview)

## RAG evaluation

- Microsoft's documentation distinguishes evaluation of retrieved documents from evaluation of response groundedness, relevance, and completeness. [RAG evaluators](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/rag-evaluators)

## Contextual retrieval and Elasticsearch

- Anthropic describes generating chunk-specific context from the source document and prepending it before both embedding and BM25 indexing. The cookbook contains the corresponding implementation. [Original contextual retrieval method](https://www.anthropic.com/research/contextual-retrieval) · [Official contextual embeddings cookbook](https://platform.claude.com/cookbook/capabilities-contextual-embeddings-guide)
- Elasticsearch documents text analysis, exact-value metadata, and dense vector mappings. These define the fields in the teaching schema. [Standard analyzer](https://www.elastic.co/docs/reference/text-analysis/analysis-standard-analyzer) · [Keyword fields](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/keyword) · [Dense vector fields](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/dense-vector)
- Elasticsearch documents its default BM25 parameters, and Lucene's source implements the IDF and saturating term-frequency factor. Stanford's IR textbook covers TF-IDF variants. [Similarity settings](https://www.elastic.co/docs/reference/elasticsearch/index-settings/similarity) · [Lucene BM25 source](https://github.com/apache/lucene/blob/main/lucene/core/src/java/org/apache/lucene/search/similarities/BM25Similarity.java) · [Introduction to Information Retrieval, Chapter 6](https://nlp.stanford.edu/IR-book/pdf/irbookonlinereading.pdf)
- Lucene's BM25 API explicitly describes term frequency saturation, document length normalization, and IDF. Checked on November 22 for the retrieval relationship diagram. [BM25Similarity API](https://lucene.apache.org/core/10_3_1/core/org/apache/lucene/search/similarities/BM25Similarity.html)
- Elasticsearch provides separate lexical and vector queries plus rank fusion. Its inspection APIs expose analysis output, term statistics, and score explanations. [Match query](https://www.elastic.co/docs/reference/query-languages/query-dsl/query-dsl-match-query) · [kNN query](https://www.elastic.co/docs/reference/query-languages/query-dsl/query-dsl-knn-query) · [RRF retriever](https://www.elastic.co/docs/reference/elasticsearch/rest-apis/retrievers/rrf-retriever) · [Analyze API](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-analyze) · [Term vectors API](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-termvectors) · [Explain API](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-explain)
- Elastic describes its deployed BM25 and ELSER support assistants and reports the effect of retrieval relevance on answer quality. This provides the production example, while the Orders API dataset is a mentor-created illustration. [Production lessons](https://www.elastic.co/blog/building-ai-agents-elasticsearch-platform)
- The Lecture 3 PDF refresh failed with a connection reset on November 20. The previously recorded contextual retrieval pages remain PDF pages 26–29. The original method and current Elasticsearch documentation were accessible for this explanation.
- Elasticsearch documents analyzed text indexing and the RRF retriever's filter, which applies to its child retrievers. These support the complete hybrid request added on November 22. [Text fields](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/text) · [RRF retriever and shared filtering](https://www.elastic.co/docs/reference/elasticsearch/rest-apis/retrievers/rrf-retriever)

## Approximate vector search and quantization

- Elasticsearch distinguishes approximate indexed kNN from exact brute-force retrieval and documents HNSW and quantized vector formats. [kNN retrieval](https://www.elastic.co/docs/solutions/search/vector/knn) · [Dense vector index options](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/dense-vector)
- Malkov and Yashunin introduce the hierarchical navigable proximity graphs used for HNSW search. Faiss documents product quantization and its vector index implementations. [HNSW paper](https://arxiv.org/abs/1603.09320) · [Faiss research foundations](https://faiss.ai/index.html) · [Faiss index types](https://github.com/facebookresearch/faiss/wiki/Faiss-indexes)
- Faiss's product quantizer reference describes k-means training, per-subspace centroids, code computation, and query distance tables. [ProductQuantizer reference](https://faiss.ai/cpp_api/struct/structfaiss_1_1ProductQuantizer.html)
- Faiss documents inverted file indexing, cluster assignments, and multi-probe searches across selected lists. [IndexIVF reference](https://faiss.ai/cpp_api/struct/structfaiss_1_1IndexIVF.html)
- The Elasticsearch dense vector documentation was rechecked on November 22 to distinguish general algorithm names from mapping values. It lists HNSW variants and a clustering-based `bbq_disk` option, with availability depending on version and configuration. The learning diagram uses general roles rather than asserting that `ivf` is a mapping value. [Current vector index options](https://www.elastic.co/docs/reference/elasticsearch/mapping-reference/dense-vector)

## Late chunking

- Lecture 3 introduces late chunking on PDF pages 30–31. Section 3 and Figure 2 of the original paper describe encoding the full input into token representations before pooling by chunk. Table 1 contains the Berlin example. Section 3.1 extends the approach to overlapping larger windows. This is a reference for the learner's question, with no additional reading task assigned. [Late Chunking paper](https://arxiv.org/html/2409.04701v3)
- The authors' repository contains the chunked pooling implementation and the worked contextual embedding example. [Jina late-chunking repository](https://github.com/jina-ai/late-chunking) · [Author's introduction](https://jina.ai/news/late-chunking-in-long-context-embedding-models/)

## Embedding encoder and pooling

- Sections 3.1–3.5 of the original Transformer paper describe the encoder blocks, query-key-value attention, feed-forward networks, token embeddings, and position information. [Attention Is All You Need](https://arxiv.org/html/1706.03762)
- Jina's model card describes its BERT-based bidirectional embedding encoder and mean pooling. It grounds the short-text example in the type of embedding model used for late chunking. [Jina embeddings v2 model card](https://huggingface.co/jinaai/jina-embeddings-v2-base-en)
- Hugging Face explains how tokenizers use a vocabulary and learned splitting or merge rules to map new text into tokens. The miniature calculation uses a deliberately simple constructed vocabulary. [BPE tokenization](https://huggingface.co/learn/llm-course/en/chapter6/5)
- PyTorch documents embedding tables as index-based lookup and gives the layer normalization formula, affine parameters, and epsilon. These support the complete numerical example. [Embedding](https://docs.pytorch.org/docs/2.15/generated/torch.nn.Embedding.html) · [LayerNorm](https://docs.pytorch.org/docs/2.15/generated/torch.nn.LayerNorm.html)

## RAPTOR

- Lecture 3 introduces hierarchical indexing with RAPTOR on PDF page 32. Figure 1 and Section 3 of the original paper describe recursive embedding, clustering, and summarization. Figure 2 compares tree traversal with collapsed-tree retrieval. [Lecture 3 slides](https://web.stanford.edu/class/cs329z/slides/lecture03.pdf#page=32) · [RAPTOR paper](https://arxiv.org/html/2401.18059v1)
- The authors' implementation exposes the tree-building and retrieval workflow and supports embedding, summarization, and answer models. This is a reference for the learner's current question. [Official RAPTOR repository](https://github.com/parthsarthi03/raptor)

## GraphRAG

- Lecture 3 introduces GraphRAG on PDF pages 34–35. Edge et al. describe extracting entity graphs and generating community summaries for corpus-level question answering. [Original GraphRAG paper](https://arxiv.org/abs/2404.16130)
- Microsoft documents entity-linked local search and map-reduce generation over community reports for global search. [Local search](https://microsoft.github.io/graphrag/query/local_search/) · [Global search](https://microsoft.github.io/graphrag/query/global_search/)

## GraphRAG storage and processing

- Microsoft documents the output table schemas and default Parquet storage. Its local-search example loads those tables and uses a LanceDB vector store. [Index output tables](https://microsoft.github.io/graphrag/index/outputs/) · [Local-search implementation example](https://microsoft.github.io/graphrag/examples_notebooks/local_search/)
- Neo4j describes hybrid retrieval over vector and full-text indexes followed by Cypher graph expansion. Its Cypher manual documents variable-length paths. [GraphRAG retrieval guide](https://neo4j.com/docs/neo4j-graphrag-python/current/user_guide_rag.html) · [Variable-length paths](https://neo4j.com/docs/cypher-manual/current/patterns/variable-length-paths/)
- Elastic demonstrates storing graph relationships as triples, retrieving by source and destination, and constructing evidence from a relevant subgraph. [Graph RAG and Elasticsearch](https://www.elastic.co/search-labs/blog/rag-graph-traversal)
- Neo4j defines its property graph model and directed typed relationships. Elasticsearch documents exact term filtering and its Graph Explore API, which explores document-term connections. These clarify the storage and hop comparison. [Neo4j graph concepts](https://neo4j.com/docs/getting-started/appendix/graphdb-concepts/) · [Elasticsearch term query](https://www.elastic.co/docs/reference/query-languages/query-dsl/query-dsl-term-query) · [Elasticsearch Graph Explore API](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-graph-explore)

## DPR

- DPR is an official Lecture 3 reading. Section 3 defines the independent question and passage encoders, CLS output vectors, dot-product scoring, and training with positive and negative passages. [Dense Passage Retrieval paper](https://arxiv.org/html/2004.04906)
- The original implementation separates passage embedding generation, dense retrieval, and encoder training, showing where the model and vector index fit in the pipeline. [Official DPR repository](https://github.com/facebookresearch/DPR)

## Retriever evaluation

- The Lecture 3 PDF was successfully retrieved and its text inspected on November 22. PDF pages 45–46 define Hit@k, Failed@k, nDCG@k, MRR@k, and Recall@k. The worked calculation follows the slide's linear relevance gain in DCG. [Lecture 3 scoring slides](https://web.stanford.edu/class/cs329z/slides/lecture03.pdf#page=45)
- Elasticsearch documents relevance judgments, evaluation query sets, recall, MRR, and DCG through its `_rank_eval` API. [Ranking evaluation](https://www.elastic.co/docs/reference/elasticsearch/rest-apis/search-rank-eval)

## Embedding model alternatives

These model cards and API documentation were checked on November 22 as references for the learner's question. They are examples to understand interchangeable pipeline roles, with no additional reading assignment or model installation requested.

- BGE-M3 supports multilingual retrieval and dense, sparse, and multi-vector representations. Its dense embedding dimension is 1024. The dense mode fits the single-vector HNSW pipeline discussed here. [BGE-M3 model card](https://huggingface.co/BAAI/bge-m3)
- multilingual-e5-large documents 1024-dimensional embeddings, query and passage prefixes, mean pooling, and normalization. These illustrate why input conventions matter even when two models have the same output width. [Multilingual E5 model card](https://huggingface.co/intfloat/multilingual-e5-large)
- Qwen3-Embedding-0.6B is an open-weight embedding model with multilingual capabilities. Its retrieval example adds a task instruction to queries and uses normalized pooled representations. [Qwen3-Embedding model card](https://huggingface.co/Qwen/Qwen3-Embedding-0.6B)
- OpenAI documents hosted text-embedding-3-small and text-embedding-3-large models, vector outputs, configurable dimensions, and token-based billing. [Embedding API guide](https://developers.openai.com/api/docs/guides/embeddings)

## Bi-encoders and cross-encoder reranking

These are references for the current question, checked on November 22, rather than additional reading assignments.

- Lecture 3 PDF page 50, labeled slide 51, contrasts independent query and passage encoding with joint encoding and full attention across both. [Course comparison](https://web.stanford.edu/class/cs329z/slides/lecture03.pdf#page=50)
- Sentence Transformers documents separate sentence embeddings, pairwise cross-encoder scoring, and the retrieve-then-rerank architecture. [Cross-encoder comparison](https://www.sbert.net/examples/cross_encoder/applications/README.html) · [Retrieve and rerank](https://www.sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html)
- The BGE reranker model card shows query-passage text pairs as input, relevance logits as output, and optional sigmoid normalization. Its checkpoint is distinct from BGE-M3's embedding checkpoint. [BGE reranker v2 M3](https://huggingface.co/BAAI/bge-reranker-v2-m3)

## Late interaction and ColBERT

These references were checked on November 22 for the current explanation. No additional reading task, model installation, or experiment is assigned.

- Lecture 3 PDF page 51, labeled slide 52, defines independent token-level representations and the sum-of-maxima score. PDF page 52 introduces the ColBERT architecture. [Late interaction slides](https://web.stanford.edu/class/cs329z/slides/lecture03.pdf#page=51)
- Sections 3.1–3.3 and Figure 3 of the original paper describe contextual token representations, projection, normalization, and MaxSim. Section 3.3 also specifies positive/negative training triples and notes that the interaction rule has no trainable parameters. Sections 3.4–3.6 explain offline passage encoding, reranking, and full-collection retrieval. Section 4.1.2 specifies the original experiments' 128-dimensional vectors. [Original ColBERT paper](https://arxiv.org/html/2004.12832)
- The authors' repository explains pretrained checkpoints, query and passage embedding matrices, MaxSim, and the indexing/search workflow. The search example returns passage IDs, ranks, and scores, distinguishing the retriever output from a generated answer. The repository distinguishes the original ColBERT implementation from later ColBERTv2 and retrieval engine work. [Official ColBERT repository](https://github.com/stanford-futuredata/ColBERT)

## Retriever comparison summary

- Lecture 3 PDF page 54, titled "Fast vs Slow Retrievers," compares BM25, DPR, ColBERT, and a BERT-base cross-encoder. The text was checked on November 22. The table's timings come from cited experiments with different hardware and workloads; retain that context when reviewing the figures. This is a reference for the requested note, with no additional reading task. [Official comparison slide](https://web.stanford.edu/class/cs329z/slides/lecture03.pdf#page=54)

## Self-RAG

These sources were checked on November 22 for the learner's current question. They are review references, with no additional reading task assigned.

- Lecture 3 PDF page 56 frames retrieval as an action inside a control loop; PDF page 57 introduces Self-RAG's retrieval, generation, and critique. [Agentic retrieval](https://web.stanford.edu/class/cs329z/slides/lecture03.pdf#page=56) · [Self-RAG slide](https://web.stanford.edu/class/cs329z/slides/lecture03.pdf#page=57)
- Table 1, Algorithm 1, and Sections 3.1–3.3 define reflection categories, per-passage generation branches, segment-level decoding, and critic/generator training. Those sections were inspected for this explanation, without claiming a full-paper review. [Original Self-RAG paper](https://arxiv.org/html/2310.11511)
- The authors' project page explains adaptive retrieval and the separation of offline critic supervision from the generator's inference-time self-reflection. [Author overview](https://selfrag.github.io/)
- The original repository shows concrete reflection-token outputs, externally inserted evidence, adaptive retrieval controls, and its default Contriever retrieval setup. These ground the explanation in the implementation. No installation or model execution was performed. [Official Self-RAG repository](https://github.com/AkariAsai/self-rag)

## CRAG and Search-R1

These sources were checked on November 22 for the current comparison. They are references for review, not additional reading assignments.

- Lecture 3 PDF page 58 introduces CRAG, followed by Search-R1 on PDF pages 59–61. [CRAG slide](https://web.stanford.edu/class/cs329z/slides/lecture03.pdf#page=58) · [Search-R1 slides](https://web.stanford.edu/class/cs329z/slides/lecture03.pdf#page=59)
- CRAG Sections 4.1–4.5 and Algorithm 1 describe the fine-tuned T5-large evaluator, score thresholds, Correct/Incorrect/Ambiguous routes, knowledge strip refinement, and supplementary web search. Relevant sections were inspected, without claiming a full-paper review. [Original CRAG paper](https://arxiv.org/html/2401.15884)
- Search-R1 Sections 3.1–3.4 define reinforcement learning with an external search engine, multi-turn tool calls, retrieved-token loss masking, and final-answer rewards. Section 4.3 identifies the Wikipedia corpus and E5 retriever. [Original Search-R1 paper](https://arxiv.org/html/2503.09516)
- The authors' implementation separates the policy LLM and retrieval service and provides inference and training workflows with an E5-backed local search setup. It documents that off-the-shelf retrievers can be selected independently. No setup commands were executed. [Official Search-R1 repository](https://github.com/PeterGriffinJin/Search-R1)

## ReAct connection for agentic retrieval

- The authors' overview explains prompted interleaving of reasoning, tool actions, and observations, including question answering with a Wikipedia API. This connects L03's adaptive retrieval to L01 rather than adding another course topic or required paper. [ReAct author overview](https://react-lm.github.io/)
