---
layout: default
---

# Recent Papers/Blogs/Tools Related to Fuzzing

The blog post contains classic fuzzing books, papers about fuzzing at information security top conferences over the years, commonly used fuzzing tools, and blogs that can quickly learn fuzzing tools.

## 1 Books

- [The Fuzzing Book](https://www.fuzzingbook.org/) (2019)：This book is based on principles + code exercises, combined with practical exercises, to complete a fuzzing test framework from 0 to 1. If you want to write your own fuzzing framework, you can refer to this book.
- [Fuzzing for Software Security Testing and Quality Assurance](https://www.amazon.com/Fuzzing-Software-Security-Testing-Assurance/dp/1608078507/) (2018)：This book introduces the idea of fuzzing into the software development life cycle. In fact, many efficient fuzzing tests are often considered in the development stage. The book discusses the development of fuzz tools, including not only some emerging open source tools, but also many commercial ones. How to choose the right fuzzer for software development projects is also one of the themes of this book.

## 2 Articles&Papers

This chapter contains top-level information security and classic papers in some journals. We just want to select some of them with relatively high technical value or relatively novel articles to facilitate subsequent learning.

### Others

- [The Art, Science, and Engineering of Fuzzing: A Survey](https://ieeexplore.ieee.org/document/8863940) (2019)
- [Fuzzing: a survey](https://cybersecurity.springeropen.com/articles/10.1186/s42400-018-0002-y) (2018)
- [Evaluating Fuzz Testing, 2018](http://www.cs.umd.edu/~mwh/papers/fuzzeval.pdf)
- [Fuzzing: Art, Science, and Engineering, 2018](https://arxiv.org/pdf/1812.00140.pdf)
- [Fuzzing: State of the art, 2018](https://ieeexplore.ieee.org/document/8371326)
- [Source-and-Fuzzing](https://github.com/lcatro/Source-and-Fuzzing) (2019)
- [CoLaFUZE: Coverage-Guided and Layout-Aware Fuzzing for Android Drivers](https://www.jstage.jst.go.jp/article/transinf/E104.D/11/E104.D_2021NGP0005/_pdf) (2021)
- [Better Pay Attention Whilst Fuzzing](https://arxiv.org/pdf/2112.07143) (2022)
- [Effective File Format Fuzzing – Thoughts, Techniques and Results](https://www.youtube.com/watch?v=qTTwqFRD1H8)

### NDSS

#### 2025

- [Automatic Library Fuzzing through API Relation Evolvement, 2025](https://www.ndss-symposium.org/ndss-paper/automatic-library-fuzzing-through-api-relation-evolvement/)
- [Blackbox Fuzzing of Distributed Systems with Multi-Dimensional Inputs and Symmetry-Based Feedback Pruning, 2025](https://www.ndss-symposium.org/ndss-paper/blackbox-fuzzing-of-distributed-systems-with-multi-dimensional-inputs-and-symmetry-based-feedback-pruning/)
- [DUMPLING: Fine-grained Differential JavaScript Engine Fuzzing, 2025](https://www.ndss-symposium.org/ndss-paper/dumpling-fine-grained-differential-javascript-engine-fuzzing/)
- [FUZZUER: Enabling Fuzzing of UEFI Interfaces on EDK-2, 2025](https://www.ndss-symposium.org/ndss-paper/fuzzuer-enabling-fuzzing-of-uefi-interfaces-on-edk-2/)
- [ICSQuartz: Scan Cycle-Aware and Vendor-Agnostic Fuzzing for Industrial Control Systems, 2025](https://www.ndss-symposium.org/ndss-paper/icsquartz-scan-cycle-aware-and-vendor-agnostic-fuzzing-for-industrial-control-systems/)
- [MALintent: Coverage Guided Intent Fuzzing Framework for Android, 2025](https://www.ndss-symposium.org/ndss-paper/malintent-coverage-guided-intent-fuzzing-framework-for-android/)
- [Moneta: Ex-Vivo GPU Driver Fuzzing by Recalling In-Vivo Execution States, 2025](https://www.ndss-symposium.org/ndss-paper/moneta-ex-vivo-gpu-driver-fuzzing-by-recalling-in-vivo-execution-states/)
- [QMSan: Efficiently Detecting Uninitialized Memory Errors During Fuzzing, 2025](https://www.ndss-symposium.org/ndss-paper/qmsan-efficiently-detecting-uninitialized-memory-errors-during-fuzzing/)
- [TWINFUZZ: Differential Testing of Video Hardware Acceleration Stacks, 2025](https://www.ndss-symposium.org/ndss-paper/twinfuzz-differential-testing-of-video-hardware-acceleration-stacks/)
- [Truman: Constructing Device Behavior Models from OS Drivers to Fuzz Virtual Devices, 2025](https://www.ndss-symposium.org/ndss-paper/truman-constructing-device-behavior-models-from-os-drivers-to-fuzz-virtual-devices/)
- [DeepGo: Predictive Directed Greybox Fuzzing, 2024](https://www.ndss-symposium.org/ndss-paper/deepgo-predictive-directed-greybox-fuzzing/)
- [EnclaveFuzz: Finding Vulnerabilities in SGX Applications, 2024](https://www.ndss-symposium.org/ndss-paper/enclavefuzz-finding-vulnerabilities-in-sgx-applications/)
- [Large Language Model guided Protocol Fuzzing, 2024](https://www.ndss-symposium.org/ndss-paper/large-language-model-guided-protocol-fuzzing/)
- [MOCK: Optimizing Kernel Fuzzing Mutation with Context-aware Dependency, 2024](https://www.ndss-symposium.org/ndss-paper/mock-optimizing-kernel-fuzzing-mutation-with-context-aware-dependency/)
- [Predictive Context-sensitive Fuzzing, 2024](https://www.ndss-symposium.org/ndss-paper/predictive-context-sensitive-fuzzing/)
- [ReqsMiner: Automated Discovery of CDN Forwarding Request Inconsistencies and DoS Attacks with Grammar-based Fuzzing, 2024](https://www.ndss-symposium.org/ndss-paper/reqsminer-automated-discovery-of-cdn-forwarding-request-inconsistencies-and-dos-attacks-with-grammar-based-fuzzing/)
- [ShapFuzz: Efficient Fuzzing via Shapley-Guided Byte Selection, 2024](https://www.ndss-symposium.org/ndss-paper/shapfuzz-efficient-fuzzing-via-shapley-guided-byte-selection/)
- [Assessing the Impact of Interface Vulnerabilities in Compartmentalized Software, 2023](https://www.ndss-symposium.org/ndss-paper/assessing-the-impact-of-interface-vulnerabilities-in-compartmentalized-software/)
- [FUZZILLI: Fuzzing for JavaScript JIT Compiler Vulnerabilities, 2023](https://www.ndss-symposium.org/ndss-paper/fuzzilli-fuzzing-for-javascript-jit-compiler-vulnerabilities/)
- [No Grammar, No Problem: Towards Fuzzing the Linux Kernel without System-Call Descriptions, 2023](https://www.ndss-symposium.org/ndss-paper/no-grammar-no-problem-towards-fuzzing-the-linux-kernel-without-system-call-descriptions/)
- [DARWIN: Survival of the Fittest Fuzzing Mutators, 2023](https://www.ndss-symposium.org/ndss-paper/darwin-survival-of-the-fittest-fuzzing-mutators/)
- [LOKI: State-Aware Fuzzing Framework for the Implementation of Blockchain Consensus Protocols, 2023](https://www.ndss-symposium.org/ndss-paper/loki-state-aware-fuzzing-framework-for-the-implementation-of-blockchain-consensus-protocols/)
- [OBSan: An Out-Of-Bound Sanitizer to Harden DNN Executables, 2023](https://www.ndss-symposium.org/ndss-paper/obsan-an-out-of-bound-sanitizer-to-harden-dnn-executables/)
- [MobFuzz: Adaptive Multi-objective Optimization in Gray-box Fuzzing](https://www.ndss-symposium.org/ndss-paper/auto-draft-199/) (2022)
- [FirmWire: Transparent Dynamic Analysis for Cellular Baseband Firmware](https://hernan.de/research/papers/firmwire-ndss22-hernandez.pdf) (2022)
- [EMS: History-Driven Mutation for Coverage-based Fuzzing](https://nesa.zju.edu.cn/download/lcy_pdf_ems_ndss22.pdf) (2022)
- [Context-Sensitive and Directional Concurrency Fuzzing for Data-Race Detection](https://www.ndss-symposium.org/ndss-paper/auto-draft-198/) (2022) 
- [datAFLow: Towards a Data-Flow-Guided Fuzzer](https://www.ndss-symposium.org/ndss-paper/auto-draft-273/) (2022)
- [Favocado: Fuzzing the Binding Code of JavaScript Engines Using Semantically Correct Test Cases](https://www.ndss-symposium.org/ndss-paper/favocado-fuzzing-the-binding-code-of-javascript-engines-using-semantically-correct-test-cases/) (2021)
- [WINNIE : Fuzzing Windows Applications with Harness Synthesis and Fast Cloning, 2021](https://www.ndss-symposium.org/ndss-paper/winnie-fuzzing-windows-applications-with-harness-synthesis-and-fast-cloning/)
- [PGFUZZ: Policy-Guided Fuzzing for Robotic Vehicles](https://www.ndss-symposium.org/ndss-paper/pgfuzz-policy-guided-fuzzing-for-robotic-vehicles/) (2021)
- [Reinforcement Learning-based Hierarchical Seed Scheduling for Greybox Fuzzing](https://www.ndss-symposium.org/ndss-paper/reinforcement-learning-based-hierarchical-seed-scheduling-for-greybox-fuzzing/) (2021)
- [HFL: Hybrid Fuzzing on the Linux Kernel](https://www.unexploitable.systems/publication/kimhfl/) (2020)
- [HotFuzz: Discovering Algorithmic Denial-of-Service Vulnerabilities Through Guided Micro-Fuzzing](https://www.researchgate.net/publication/339164746_HotFuzz_Discovering_Algorithmic_Denial-of-Service_Vulnerabilities_Through_Guided_Micro-Fuzzing) (2020)
- [Not All Coverage Measurements Are Equal: Fuzzing by Coverage Accounting for Input Prioritization](https://www.ndss-symposium.org/wp-content/uploads/2020/02/24422.pdf) (2020)
- [PeriScope: An Effective Probing and Fuzzing Framework for the Hardware-OS Boundary](https://people.cs.kuleuven.be/~stijn.volckaert/papers/2019_NDSS_PeriScope.pdf) (2019)
- [INSTRIM: Lightweight Instrumentation for Coverage-guided Fuzzing](https://www.ndss-symposium.org/wp-content/uploads/2018/07/bar2018_14_Hsu_paper.pdf) (2018)
- [What You Corrupt Is Not What You Crash: Challenges in Fuzzing Embedded Devices](http://s3.eurecom.fr/docs/ndss18_muench.pdf)
- [Enhancing Memory Error Detection for Large-Scale Applications and Fuzz Testing](https://lifeasageek.github.io/papers/han:meds.pdf) (2018)
- [DELTA: A Security Assessment Framework for Software-Defined Networks](https://www.ndss-symposium.org/wp-content/uploads/2017/09/ndss201702A-1LeePaper.pdf) (2017)

### USENIX Security

- [A Binary-level Thread Sanitizer or Why Sanitizing on the Binary Level is Hard, 2024](https://www.usenix.org/conference/usenixsecurity24/presentation/schilling)
- [Critical Code Guided Directed Greybox Fuzzing for Commits, 2024](https://www.usenix.org/conference/usenixsecurity24/presentation/xiang-yi)
- [EL3XIR: Fuzzing COTS Secure Monitors, 2024](https://www.usenix.org/conference/usenixsecurity24/presentation/lindenmeier)
- [Fuzzing BusyBox: Leveraging LLM and Crash Reuse for Embedded Bug Unearthing, 2024](https://www.usenix.org/conference/usenixsecurity24/presentation/asmita)
- [HYPERPILL: Fuzzing for Hypervisor-bugs by leveraging the Hardware Virtualization Interface, 2024](https://www.usenix.org/conference/usenixsecurity24/presentation/bulekov)
- [MultiFuzz: A Multi-Stream Fuzzer For Testing Monolithic Firmware, 2024](https://www.usenix.org/conference/usenixsecurity24/presentation/chesser)
- [SDFuzz: Target States Driven Directed Fuzzing, 2024](https://www.usenix.org/conference/usenixsecurity24/presentation/li-penghui)
- [SHiFT: Semi-hosted Fuzz Testing for Embedded Applications, 2024](https://www.usenix.org/conference/usenixsecurity24/presentation/mera)
- [Towards Generic Database Management System Fuzzing, 2024](https://www.usenix.org/conference/usenixsecurity24/presentation/yang-yupeng)
- [WhisperFuzz: White-Box Fuzzing for Detecting and Locating Timing Vulnerabilities in Processors, 2024](https://www.usenix.org/conference/usenixsecurity24/presentation/borkar)
- [Fuzztruction: Using Fault Injection-based Fuzzing to Leverage Implicit Domain Knowledge, 2023](https://www.usenix.org/conference/usenixsecurity23/presentation/bars)
- [DynSQL: Stateful Fuzzing for Database Management Systems with Complex and Valid SQL Query Generation, 2023](https://www.usenix.org/conference/usenixsecurity23/presentation/jiang-zu-ming)
- [FuzzJIT: Oracle-Enhanced Fuzzing for JavaScript Engine JIT Compiler, 2023](https://www.usenix.org/conference/usenixsecurity23/presentation/wang-junjie)
- [GLeeFuzz: Fuzzing WebGL Through Error Message Guided Mutation, 2023](https://www.usenix.org/conference/usenixsecurity23/presentation/peng)
- [Automata-Guided Control-Flow-Sensitive Fuzz Driver Generation, 2023](https://www.usenix.org/conference/usenixsecurity23/presentation/zhang-cen)
- [PolyFuzz: Holistic Greybox Fuzzing of Multi-Language Systems, 2023](https://www.usenix.org/conference/usenixsecurity23/presentation/li-wen)
- [AIFORE: Smart Fuzzing Based on Automatic Input Format Reverse Engineering, 2023](https://www.usenix.org/conference/usenixsecurity23/presentation/shi-ji)
- [Remote Code Execution from SSTI in the Sandbox: Automatically Detecting and Exploiting Template Escape Bugs, 2023](https://www.usenix.org/conference/usenixsecurity23/presentation/zhao-yudi)
- [MTSan: A Feasible and Practical Memory Sanitizer for Fuzzing COTS Binaries, 2023](https://www.usenix.org/conference/usenixsecurity23/presentation/chen-xingman)
- [MorFuzz: Fuzzing Processor via Runtime Instruction Morphing enhanced Synchronizable Co-simulation, 2023](https://www.usenix.org/conference/usenixsecurity23/presentation/xu-jinyan)
- [MINER: A Hybrid Data-Driven Approach for REST API Fuzzing, 2023](https://www.usenix.org/conference/usenixsecurity23/presentation/lyu)
- [KextFuzz: Fuzzing macOS Kernel EXTensions on Apple Silicon via Exploiting Mitigations, 2023](https://www.usenix.org/conference/usenixsecurity23/presentation/yin)
- [Intender: Fuzzing Intent-Based Networking with Intent-State Transition Guidance, 2023](https://www.usenix.org/conference/usenixsecurity23/presentation/kim-jiwon)
- [DDRace: Finding Concurrency UAF Vulnerabilities in Linux Drivers with Directed Fuzzing, 2023](https://www.usenix.org/conference/usenixsecurity23/presentation/yuan-ming)
- [CarpetFuzz: Automatic Program Option Constraint Extraction from Documentation for Fuzzing, 2023](https://www.usenix.org/conference/usenixsecurity23/presentation/wang-dawei)
- [BoKASAN: Binary-only Kernel Address Sanitizer for Effective Kernel Fuzzing, 2023](https://www.usenix.org/conference/usenixsecurity23/presentation/cho)
- [Bleem: Packet Sequence Oriented Fuzzing for Protocol Implementations, 2023](https://www.usenix.org/conference/usenixsecurity23/presentation/luo-zhengxiong)
- [autofz: Automated Fuzzer Composition at Runtime, 2023](https://www.usenix.org/conference/usenixsecurity23/presentation/fu-yu-fu)
- [MundoFuzz: Hypervisor Fuzzing with Statistical Coverage Testing and Grammar Inference, 2022](https://www.usenix.org/conference/usenixsecurity22/presentation/myung)
- [TheHuzz: Instruction Fuzzing of Processors Using Golden-Reference Models for Finding Software-Exploitable Vulnerabilities, 2022](https://arxiv.org/abs/2201.09941)
- [Morphuzz: Bending (Input) Space to Fuzz Virtual Devices, 2022](https://www.usenix.org/conference/usenixsecurity22/presentation/bulekov)
- [Fuzzware: Using Precise MMIO Modeling for Effective Firmware Fuzzing, 2022](https://www.usenix.org/conference/usenixsecurity22/presentation/scharnowski)
- [FuzzOrigin: Detecting UXSS vulnerabilities in Browsers through Origin Fuzzing, 2022](https://www.usenix.org/conference/usenixsecurity22/presentation/kim)
- [Drifuzz: Harvesting Bugs in Device Drivers from Golden Seeds, 2022](https://www.usenix.org/conference/usenixsecurity22/presentation/shen-zekun)
- [Fuzzing Hardware Like Software, 2022](https://www.usenix.org/conference/usenixsecurity22/presentation/trippel)
- [BrakTooth: Causing Havoc on Bluetooth Link Manager via Directed Fuzzing, 2022](https://www.usenix.org/conference/usenixsecurity22/presentation/garbelini)
- [AmpFuzz: Fuzzing for Amplification DDoS Vulnerabilities, 2022](https://www.usenix.org/conference/usenixsecurity22/presentation/krupp)
- [SGXFuzz: Efficiently Synthesizing Nested Structures for SGX Enclave Fuzzing, 2022](https://www.usenix.org/conference/usenixsecurity22/presentation/cloosters)
- [FRAMESHIFTER: Manipulating HTTP/2 Frame Sequences with Fuzzing, 2022](https://www.usenix.org/conference/usenixsecurity22/presentation/jabiyev)
- [FIXREVERTER: A Realistic Bug Injection Methodology for Benchmarking Fuzz Testing, 2022](https://www.usenix.org/conference/usenixsecurity22/presentation/zhang-zenong)
- [StateFuzz: System Call-Based State-Aware Linux Driver Fuzzing, 2022](https://www.usenix.org/conference/usenixsecurity22/presentation/zhao-bodong)
- [SyzScope: Revealing High-Risk Security Impacts of Fuzzer-Exposed Bugs inLinux kernel, 2022](https://www.usenix.org/system/files/sec22summer_zou.pdf)
- [Automatic Firmware Emulation through Invalidity-guided Knowledge Inference, 2021](https://www.usenix.org/conference/usenixsecurity21/presentation/zhou)
- [Constraint-guided Directed Greybox Fuzzing, 2021](https://www.usenix.org/conference/usenixsecurity21/presentation/lee-gwangmu)
- [UNIFUZZ: A Holistic and Pragmatic Metrics-Driven Platform for Evaluating Fuzzers, 2021](https://www.usenix.org/biblio-6129)
- [Nyx: Greybox Hypervisor Fuzzing using Fast Snapshots and Affine Types, 2021](https://www.usenix.org/conference/usenixsecurity21/presentation/schumilo)
- [Breaking Through Binaries: Compiler-quality Instrumentation for Better Binary-only Fuzzing, 2021](https://www.usenix.org/conference/usenixsecurity21/presentation/nagy)
- [The Use of Likely Invariants as Feedback for Fuzzers, 2021](https://www.usenix.org/conference/usenixsecurity21/presentation/fioraldi)
- [Analysis of DTLS Implementations Using Protocol State Fuzzing](https://www.usenix.org/conference/usenixsecurity20/presentation/fiterau-brostean) 
- [EcoFuzz: Adaptive Energy-Saving Greybox Fuzzing as a Variant of the Adversarial Multi-Armed Bandit](https://www.usenix.org/conference/usenixsecurity20/presentation/yue) (2020)
- [FANS: Fuzzing Android Native System Services via Automated Interface Analysis](https://www.usenix.org/conference/usenixsecurity20/presentation/liu) (2020)
- [Fuzzing Error Handling Code using Context-Sensitive Software Fault Injection](https://www.usenix.org/conference/usenixsecurity20/presentation/jiang) (2020)
- [FuzzGen: Automatic Fuzzer Generation, 2020](https://www.usenix.org/conference/usenixsecurity20/presentation/ispoglou)
- [GREYONE: Data Flow Sensitive Fuzzing, 2020](https://www.usenix.org/conference/usenixsecurity20/presentation/gan)
- [Fuzzification: Anti-Fuzzing Techniques, 2019](https://www.usenix.org/conference/usenixsecurity19/presentation/jung)
- [AntiFuzz: Impeding Fuzzing Audits of Binary Executables, 2019](https://www.usenix.org/conference/usenixsecurity19/presentation/guler)
- [MoonShine: Optimizing OS Fuzzer Seed Selection with Trace Distillation, 2018](https://www.usenix.org/conference/usenixsecurity18/presentation/pailoor)
- [QSYM : A Practical Concolic Execution Engine Tailored for Hybrid Fuzzing, 2018](https://www.usenix.org/conference/usenixsecurity18/presentation/yun)
- [OSS-Fuzz - Google's continuous fuzzing service for open source software, 2017](https://www.usenix.org/conference/usenixsecurity17/technical-sessions/presentation/serebryany)
- [kAFL: Hardware-Assisted Feedback Fuzzing for OS Kernels, 2017](https://www.usenix.org/conference/usenixsecurity17/technical-sessions/presentation/schumilo)

### IEEE S&P

- [AFGen: Whole-Function Fuzzing for Applications and Libraries, 2024](https://www.computer.org/csdl/proceedings-article/sp/2024/313000a011/1RjE9PjiDss)
- [Chronos: Finding Timeout Bugs in Practical Distributed Systems by Deep-Priority Fuzzing with Transient Delay, 2024](https://www.computer.org/csdl/proceedings-article/sp/2024/313000a109/1Ub23heRtUA)
- [DY Fuzzing: Formal Dolev-Yao Models Meet Cryptographic Protocol Fuzz Testing, 2024](https://www.computer.org/csdl/proceedings-article/sp/2024/313000a096/1Ub234bjuWA)
- [LABRADOR: Response Guided Directed Fuzzing for Black-box IoT Devices, 2024](https://www.computer.org/csdl/proceedings-article/sp/2024/313000a127/1Ub23HQTJ1C)
- [Predecessor-aware Directed Greybox Fuzzing, 2024](https://www.computer.org/csdl/proceedings-article/sp/2024/313000a040/1RjEaeMELbq)
- [SATURN: Host-Gadget Synergistic USB Driver Fuzzing, 2024](https://www.computer.org/csdl/proceedings-article/sp/2024/313000a051/1RjEaqzRsfC)
- [SoK: Prudent Evaluation Practices for Fuzzing, 2024](https://www.computer.org/csdl/proceedings-article/sp/2024/313000a137/1Ub23V26Svm)
- [SyzTrust: State-aware Fuzzing on Trusted OS Designed for IoT Devices, 2024](https://www.computer.org/csdl/proceedings-article/sp/2024/313000a070/1RjEaG9OpTa)
- [Titan: Efficient Multi-target Directed Greybox Fuzzing, 2024](https://www.computer.org/csdl/proceedings-article/sp/2024/313000a059/1RjEaxqvmQ8)
- [To Boldly Go Where No Fuzzer Has Gone Before: Finding Bugs in Linux' Wireless Stacks through VirtIO Devices, 2024](https://www.computer.org/csdl/proceedings-article/sp/2024/313000a024/1RjEa0y9RMQ)
- [DEVFUZZ: Automatic Device Model-Guided Device Driver Fuzzing, 2023](https://www.computer.org/csdl/pds/api/csdl/proceedings/download-article/1Nrc0AgBCgM/pdf)
- [ODDFUZZ: Discovering Java Deserialization Vulnerabilities via Structure-Aware Directed Greybox Fuzzing, 2023](https://arxiv.org/abs/2304.04233)
- [Finding Specification Blind Spots via Fuzz Testing, 2023](https://cs.uwaterloo.ca/~m285xu/assets/publication/fast-paper.pdf)
- [RSFuzzer: Discovering Deep SMI Handler Vulnerabilities in UEFI Firmware with Hybrid Fuzzing, 2023](https://www.computer.org/csdl/pds/api/csdl/proceedings/download-article/1Js0Ek1SE6c/pdf)
- [SegFuzz: Segmentizing Thread Interleaving to Discover Kernel Concurrency Bugs through Fuzzing, 2023](https://www.computer.org/csdl/pds/api/csdl/proceedings/download-article/1NrbZrWlldK/pdf)
- [SelectFuzz: Efficient Directed Fuzzing with Selective Path Exploration, 2023](https://www.computer.org/csdl/pds/api/csdl/proceedings/download-article/1Js0DBwgpwY/pdf)
- [TEEzz: Fuzzing Trusted Applications on COTS Android Devices, 2023](https://www.computer.org/csdl/pds/api/csdl/proceedings/download-article/1He7XWu6nJe/pdf)
- [UTOPIA: Automatic Generation of Fuzz Driver using Unit Tests, 2023](https://www.computer.org/csdl/pds/api/csdl/proceedings/download-article/1He7YBzoF0c/pdf)
- [VIDEZZO: Dependency-aware Virtual Device Fuzzing, 2023](https://www.computer.org/csdl/pds/api/csdl/proceedings/download-article/1Nrc0ztdpDy/pdf)
- [Toss a Fault to Your Witcher: Applying Grey-box Coverage-Guided Mutational Fuzzing to Detect SQL and Command Injection Vulnerabilities, 2023](https://www.computer.org/csdl/proceedings-article/sp/2023/933600a116/1He7XPiaynS)
- [JIGSAW: Efficient and Scalable Path Constraints Fuzzing, 2022](https://www.cs.ucr.edu/~heng/pubs/jigsaw_sp22.pdf)
- [PATA: Fuzzing with Path Aware Taint Analysis, 2022](http://www.wingtecher.com/themes/WingTecherResearch/assets/papers/sp22.pdf)
- [FuzzUSB: Hybrid Stateful Fuzzing of USB Gadget Stacks, 2022](https://ieeexplore.ieee.org/document/9833593)
- [Effective Seed Scheduling for Fuzzing with Graph Centrality Analysis, 2022](https://arxiv.org/abs/2203.12064),
- [BEACON: Directed Grey-Box Fuzzing with Provable Path Pruning, 2022](https://qingkaishi.github.io/public_pdfs/SP22.pdf)
- [DiFuzzRTL: Differential Fuzz Testing to Find CPU Bugs, 2021](https://ieeexplore.ieee.org/document/9519470)
- [StochFuzz: Sound and Cost-effective Fuzzing of Stripped Binaries by Incremental and Stochastic Rewriting, 2021](https://ieeexplore.ieee.org/document/9519407)
- [NtFuzz: Enabling Type-Aware Kernel Fuzzing on Windows with Static Binary Analysis, 2021](https://ieeexplore.ieee.org/document/9519448)
- [Diane: Identifying Fuzzing Triggers in Apps to Generate Under-constrained Inputs for IoT Devices, 2021](https://ieeexplore.ieee.org/document/9519432)
- [One Engine to Fuzz 'em All: Generic Language Processor Testing with Semantic Validation, 2021](https://ieeexplore.ieee.org/document/9519403)
- [IJON: Exploring Deep State Spaces via Fuzzing, 2020](https://www.syssec.ruhr-uni-bochum.de/media/emma/veroeffentlichungen/2020/02/27/IJON-Oakland20.pdf)
- [Krace: Data Race Fuzzing for Kernel File Systems, 2020](https://www.cc.gatech.edu/~mxu80/pubs/xu:krace.pdf)
- [Pangolin:Incremental Hybrid Fuzzing with Polyhedral Path Abstraction, 2020](https://qingkaishi.github.io/public_pdfs/SP2020.pdf) 
- [RetroWrite: Statically Instrumenting COTS Binaries for Fuzzing and Sanitization, 2020](https://www.semanticscholar.org/paper/RetroWrite%3A-Statically-Instrumenting-COTS-Binaries-Dinesh-Burow/845cafb153b0e4b9943c6d9b6a7e42c14845a0d6)
- [Full-speed Fuzzing: Reducing Fuzzing Overhead through Coverage-guided Tracing, 2019](https://www.computer.org/csdl/proceedings-article/sp/2019/666000b122/19skgbGVFEQ)
- [Fuzzing File Systems via Two-Dimensional Input Space Exploration, 2019](https://www.computer.org/csdl/proceedings-article/sp/2019/666000a594/19skfLYOpaw)
- [NEUZZ: Efficient Fuzzing with Neural Program Smoothing, 2019](https://www.computer.org/csdl/proceedings-article/sp/2019/666000a900/19skg5XghG0)
- [Razzer: Finding Kernel Race Bugs through Fuzzing, 2019](https://www.computer.org/csdl/proceedings-article/sp/2019/666000a296/19skfwZLirm)
- [Angora: Efficient Fuzzing by Principled Search, 2018](http://web.cs.ucdavis.edu/~hchen/paper/chen2018angora.pdf)
- [CollAFL: Path Sensitive Fuzzing, 2018](http://chao.100871.net/papers/oakland18.pdf)
- [T-Fuzz: fuzzing by program transformation, 2018](https://nebelwelt.net/publications/files/18Oakland.pdf)
- [Skyfire: Data-Driven Seed Generation for Fuzzing, 2017](https://www.ieee-security.org/TC/SP2017/papers/42.pdf)

### ACM CCS

- [LIFTFUZZ: Validating Binary Lifters through Context-aware Fuzzing with GPT, 2024](https://dl.acm.org/doi/10.1145/3658644.3670276)
- [https://github.com/zyt755/LIFTFUZZ, 2024](https://dl.acm.org/doi/10.1145/3658644.3670278)
- [RANsacked: A Domain-Informed Approach for Fuzzing LTE and 5G RAN-Core Interfaces, 2024](https://dl.acm.org/doi/10.1145/3658644.3670320)
- [RIoTFuzzer: Companion App Assisted Remote Fuzzing for Detecting Vulnerabilities in IoT Devices, 2024](https://dl.acm.org/doi/10.1145/3658644.3670342)
- [On Understanding and Forecasting Fuzzers Performance with Static Analysis, 2024](https://dl.acm.org/doi/10.1145/3658644.3670348)
- [FOX: Coverage-guided Fuzzing as Online Stochastic Control, 2024](https://dl.acm.org/doi/10.1145/3643659.3648562)
- [Prompt Fuzzing for Fuzz Driver Generation, 2024](https://arxiv.org/abs/2312.17677)
- [DarthShader: Fuzzing WebGPU Shader Translators & Compilers, 2024](https://dl.acm.org/doi/10.1145/3658644.3690209)
- [Collapse Like A House of Cards: Hacking Building Automation System Through Fuzzing, 2024](https://dl.acm.org/doi/10.1145/3658644.3690216)
- [OSmart: Whitebox Program Option Fuzzing, 2024](https://dl.acm.org/doi/10.1145/3658644.3690228)
- [Program Environment Fuzzing, 2024](https://dl.acm.org/doi/10.1145/3658644.3690229)
- [ProphetFuzz: Fully Automated Prediction and Fuzzing of High-Risk Option Combinations with Only Documentation via Large Language Model, 2024](https://dl.acm.org/doi/10.1145/3658644.3690231)
- [Leveraging Binary Coverage for Effective Generation Guidance in Kernel Fuzzing, 2024](https://dl.acm.org/doi/10.1145/3658644.3690232)
- [Toss a Fault to BpfChecker: Revealing Implementation Flaws for eBPF runtimes with Differential Fuzzing, 2024](https://dl.acm.org/doi/10.1145/3658644.3690237)
- [No Peer, no Cry: Network Application Fuzzing via Fault Injection, 2024](https://dl.acm.org/doi/10.1145/3658644.3690274)
- [Fuzz to the Future: Uncovering Occluded Future Vulnerabilities via Robust Fuzzing, 2024](https://dl.acm.org/doi/10.1145/3658644.3690278)
- [CountDown: Refcount-guided Fuzzing for Exposing Temporal Memory Errors in Linux Kernel, 2024](https://dl.acm.org/doi/10.1145/3658644.3690320)
- [Fuzzing JavaScript Engines with a Graph-based IR, 2024](https://dl.acm.org/doi/10.1145/3658644.3690336)
- [CrossFire: Fuzzing macOS Cross-XPU Memory on Apple Silicon, 2024](https://dl.acm.org/doi/10.1145/3658644.3690376)
- [DSFuzz: Detecting Deep State Bugs with Dependent State Exploration, 2023](https://dl.acm.org/doi/10.1145/3576915.3616594)
- [Fuzz on the Beach: Fuzzing Solana Smart Contracts, 2023](https://arxiv.org/abs/2309.03006)
- [Greybox Fuzzing of Distributed Systems, 2023](https://mengrj.github.io/files/CCS23.pdf)
- [HOPPER: Interpretative Fuzzing for Libraries, 2023](https://dl.acm.org/doi/10.1145/3576915.3616610)
- [Profile-guided System Optimizations for Accelerated Greybox Fuzzing, 2023](https://dl.acm.org/doi/10.1145/3576915.3616636)
- [NestFuzz: Enhancing Fuzzing with Comprehensive Understanding of Input Processing Logic, 2023](https://dl.acm.org/doi/10.1145/3576915.3623103)
- [SyzDirect: Directed Greybox Fuzzing for Linux Kernel, 2023](https://dl.acm.org/doi/10.1145/3576915.3623146)
- [PyRTFuzz: Detecting Bugs in Python Runtimes via Two-Level Collaborative Fuzzing, 2023](https://dl.acm.org/doi/10.1145/3576915.3623166)
- [Poster: Combining Fuzzing with Concolic Execution for IoT Firmware Testing, 2023](https://dl.acm.org/doi/10.1145/3576915.3624373)
- [SFuzz: Slice-based Fuzzing for Real-Time Operating Systems, 2022](https://dl.acm.org/doi/10.1145/3548606.3559367)
- [LibAFL: A Framework to Build Modular and Reusable Fuzzers, 2022](https://dl.acm.org/doi/10.1145/3548606.3560602)
- [JIT-Picking: Differential Fuzzing of JavaScript Engines, 2022](https://dl.acm.org/doi/10.1145/3548606.3560624)
- [MC2: Rigorous and Efficient Directed Greybox Fuzzing, 2022](https://dl.acm.org/doi/10.1145/3548606.3560648)
- [Favocado: Fuzzing the Binding Code of JavaScript Engines Using Semantically Correct Test Cases, 2021](https://www.ndss-symposium.org/ndss-paper/favocado-fuzzing-the-binding-code-of-javascript-engines-using-semantically-correct-test-cases/)
- [WINNIE : Fuzzing Windows Applications with Harness Synthesis and Fast Cloning, 2021](https://www.ndss-symposium.org/ndss-paper/winnie-fuzzing-windows-applications-with-harness-synthesis-and-fast-cloning/)
- [PGFUZZ: Policy-Guided Fuzzing for Robotic Vehicles, 2021](https://www.ndss-symposium.org/ndss-paper/pgfuzz-policy-guided-fuzzing-for-robotic-vehicles/)
- [Reinforcement Learning-based Hierarchical Seed Scheduling for Greybox Fuzzing, 2021](https://www.ndss-symposium.org/ndss-paper/reinforcement-learning-based-hierarchical-seed-scheduling-for-greybox-fuzzing/)
- [DIFUZE: Interface Aware Fuzzing for Kernel Drivers, 2017](https://acmccs.github.io/papers/p2123-corinaA.pdf) 
- [Learning to Fuzz from Symbolic Execution with Application to Smart Contracts, 2019](https://files.sri.inf.ethz.ch/website/papers/ccs19-ilf.pdf)
- [Matryoshka: fuzzing deeply nested branches, 2019](https://web.cs.ucdavis.edu/~hchen/paper/chen2019matryoshka.pdf)
- [Hawkeye: Towards a Desired Directed Grey-box Fuzzer, 2018](https://chenbihuan.github.io/paper/ccs18-chen-hawkeye.pdf)
- [IMF: Inferred Model-based Fuzzer, 2017](http://daramg.gift/paper/han-ccs2017.pdf)
- [SemFuzz: Semantics-based Automatic Generation of Proof-of-Concept Exploits, 2017](https://www.informatics.indiana.edu/xw7/papers/p2139-you.pdf)
- [Directed Greybox Fuzzing, 2017](https://dl.acm.org/citation.cfm?id=3134020)
- [SlowFuzz: Automated Domain-Independent Detection of Algorithmic Complexity Vulnerabilities, 2017](https://arxiv.org/pdf/1708.08437.pdf)
- [DIFUZE: Interface Aware Fuzzing for Kernel Drivers, 2017](https://acmccs.github.io/papers/p2123-corinaA.pdf)

## 3 Tools

Common and practical tools are included here, most of which have been practiced by the author and have a certain degree of universality. There are also some excellent tools that have not been maintained and updated for a long time and have very limited applicable scenarios, which are not included.

### Mutator

- [Radamsa](https://gitlab.com/akihe/radamsa): Radamsa is a test case generator for robustness testing, a.k.a. a fuzzer. It is typically used to test how well a program can withstand malformed and potentially malicious inputs. It works by reading sample files of valid data and generating interestringly different outputs from them. The main selling points of radamsa are that it has already found a slew of bugs in programs that actually matter, it is easily scriptable and, easy to get up and running. 
- [zzuf](https://github.com/samhocevar/zzuf): zzuf is a transparent application input fuzzer. It works by intercepting file operations and changing random bits in the program's input. zzuf's behaviour is deterministic, making it easy to reproduce bugs. 

### Binary

- [afl-unicorn: Fuzzing The 'Unfuzzable' ](https://www.youtube.com/watch?v=OheODvF0884): afl-unicorn lets you fuzz any piece of binary that can be emulated by Unicorn Engine. 
- [Intriguer](https://github.com/seclab-yonsei/intriguer): Intriguer is a concolic execution engine for hybrid fuzzing. The key idea of Intriguer is a field-level constraint solving, which optimizes symbolic execution with field-level information. 
- [Unicorefuzz](https://github.com/fgsect/unicorefuzz): Fuzzing the Kernel using UnicornAFL and AFL++. For details, skim through [the WOOT paper](https://www.usenix.org/system/files/woot19-paper_maier.pdf) or watch [this talk at CCCamp19](https://media.ccc.de/v/thms-32--emulate-fuzz-break-kernels). 
- [libFuzzer](http://llvm.org/docs/LibFuzzer.html): LibFuzzer is in-process, coverage-guided, evolutionary fuzzing engine. LibFuzzer is linked with the library under test, and feeds fuzzed inputs to the library via a specific fuzzing entrypoint (aka “target function”); the fuzzer then tracks which areas of the code are reached, and generates mutations on the corpus of input data in order to maximize the code coverage. The code coverage information for libFuzzer is provided by LLVM’s [SanitizerCoverage](https://clang.llvm.org/docs/SanitizerCoverage.html) instrumentation.
- [Honggfuzz](https://github.com/google/honggfuzz): A security oriented, feedback-driven, evolutionary, easy-to-use fuzzer with interesting analysis options. See the [Usage document](https://github.com/google/honggfuzz/blob/master/docs/USAGE.md) for a primer on Honggfuzz use. 
- [syzkaller](https://github.com/google/syzkaller): syzkaller is an unsupervised coverage-guided kernel fuzzer.
- [frida-fuzzer](https://github.com/andreafioraldi/frida-fuzzer):  This experimetal fuzzer is meant to be used for API in-memory fuzzing. 
- [winafl](https://github.com/googleprojectzero/winafl): A fork of AFL for fuzzing Windows binaries
- [trinity](https://github.com/kernelslacker/trinity):  Linux system call fuzzer.
- [NtCall64](https://github.com/hfiref0x/NtCall64):  Windows NT x64 syscall fuzzer .
- [kDriver-Fuzzer](https://github.com/k0keoyo/kDriver-Fuzzer): A kernel driver fuzzer, based on ioctlbf.
- [FuzzBALL](https://github.com/bitblaze-fuzzball/fuzzball): Vine-based Binary Symbolic Execution.

### API/Protocol

- [Sulley](https://github.com/OpenRCE/sulley)/[Boofuzz](https://github.com/jtpereyda/boofuzz): A fork and successor of the Sulley Fuzzing Framework 
- [fuzzowski](https://github.com/nccgroup/fuzzowski): The Network Protocol Fuzzer that we will want to use.
- [Peach](https://github.com/MozillaSecurity/peach): Peach is a fuzzing framework which uses a DSL for building fuzzers and an observer based architecture to execute and monitor them. 
- [Defensics](https://www.synopsys.com/software-integrity/security-testing/fuzz-testing.html):  Defensics is a comprehensive, versatile, automated black box fuzzer that enables organizations to efficiently and effectively discover and remediate [security weaknesses](https://www.synopsys.com/blogs/software-security/types-of-security-vulnerabilities/) in software. 
- [bsSTORM](https://beyondsecurity.com/bestorm-and-the-sdl.html?cn-reloaded=1):  Black box Fuzz Testing is a requirement of the Verification phase of the SDL, the industry-leading software security assurance process that was created by Microsoft and proven effective since 2004. 
- [API-fuzzer](https://github.com/Fuzzapi/API-fuzzer):  API Fuzzer which allows to fuzz request attributes using common pentesting techniques and lists vulnerabilities 
- [domato](https://github.com/googleprojectzero/domato): A DOM fuzzer: Written and maintained by Ivan Fratric, [ifratric@google.com](mailto:ifratric@google.com)

### Firmware

- [Forming Faster Firmware Fuzzers, 2023](https://www.usenix.org/conference/usenixsecurity23/presentation/seidel)
- [FirmSolo: Enabling dynamic analysis of binary Linux-based IoT kernel modules, 2023](https://www.usenix.org/conference/usenixsecurity23/presentation/angelakopoulos)
- [Fuzzware: Using Precise MMIO Modeling for Effective Firmware Fuzzing, 2022](https://www.usenix.org/conference/usenixsecurity22/presentation/scharnowski)
- [Automatic Firmware Emulation through Invalidity-guided Knowledge Inference, 2021](https://www.usenix.org/conference/usenixsecurity21/presentation/zhou)
- [IOTFUZZER: Discovering Memory Corruptions in IoT Through App-based Fuzzing](https://www.ndss-symposium.org/wp-content/uploads/2018/02/ndss2018_01A-1_Chen_paper.pdf)
- [FIRM-AFL: High-Throughput Greybox Fuzzing of IoT Firmware via Augmented Process Emulation](https://www.usenix.org/conference/usenixsecurity19/presentation/zheng)
- [FIRMCORN: Vulnerability-Oriented Fuzzing of IoT Firmware via Optimized Virtual Execution](https://ieeexplore.ieee.org/document/8990098)