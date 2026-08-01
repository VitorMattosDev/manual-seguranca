# ROADMAP — Manual de Seguranca da Informacao

Fila autoritativa de producao. Status: `[ ]` pendente | `[~]` em andamento | `[x]` concluido.

Commit por capitulo: `cap NNN: <titulo>` com o status atualizado no mesmo commit.


## Fase 1 — Fundamentos


### Volume 1 — Fundamentos da Segurança da Informação

- [x] **cap 001** - O que é segurança da informação - `vol01/cap001-o-que-e-seguranca-da-informacao.qmd`
- [x] **cap 002** - Os pilares: confidencialidade, integridade e disponibilidade - `vol01/cap002-os-pilares-confidencialidade-integridade-e.qmd`
- [x] **cap 003** - Autenticidade, não repúdio e responsabilização - `vol01/cap003-autenticidade-nao-repudio-e-responsabilizacao.qmd`
- [x] **cap 004** - Ativos, ameaças, vulnerabilidades e risco - `vol01/cap004-ativos-ameacas-vulnerabilidades-e-risco.qmd`
- [x] **cap 005** - Modelagem de ameaças: STRIDE, árvores de ataque e abuse cases - `vol01/cap005-modelagem-de-ameacas-stride-arvores-de-ataque.qmd`
- [x] **cap 006** - Gestão de risco: análise qualitativa e quantitativa - `vol01/cap006-gestao-de-risco-analise-qualitativa-e.qmd`
- [x] **cap 007** - Ética, legalidade e a fronteira do escopo autorizado - `vol01/cap007-etica-legalidade-e-a-fronteira-do-escopo.qmd`

### Volume 2 — Redes e Sistemas: a Base Técnica

- [x] **cap 008** - A pilha TCP/IP sob a ótica do atacante e do defensor - `vol02/cap008-a-pilha-tcp-ip-sob-a-otica-do-atacante-e-do.qmd`
- [x] **cap 009** - Endereçamento, roteamento e NAT - `vol02/cap009-enderecamento-roteamento-e-nat.qmd`
- [x] **cap 010** - Protocolos de aplicação e seus riscos: HTTP, DNS, SMTP e SNMP - `vol02/cap010-protocolos-de-aplicacao-e-seus-riscos-http.qmd`
- [x] **cap 011** - Fundamentos de sistemas operacionais: processos, permissões e memória - `vol02/cap011-fundamentos-de-sistemas-operacionais.qmd`
- [x] **cap 012** - Linux essencial para segurança - `vol02/cap012-linux-essencial-para-seguranca.qmd`
- [x] **cap 013** - Windows e Active Directory essencial - `vol02/cap013-windows-e-active-directory-essencial.qmd`
- [x] **cap 014** - Virtualização e montagem do laboratório de estudos - `vol02/cap014-virtualizacao-e-montagem-do-laboratorio-de.qmd`

### Volume 3 — Criptografia Aplicada

- [x] **cap 015** - História e princípios da criptografia - `vol03/cap015-historia-e-principios-da-criptografia.qmd`
- [x] **cap 016** - Criptografia simétrica: AES, modos de operação e AEAD - `vol03/cap016-criptografia-simetrica-aes-modos-de-operacao.qmd`
- [x] **cap 017** - Funções hash, HMAC e integridade - `vol03/cap017-funcoes-hash-hmac-e-integridade.qmd`
- [x] **cap 018** - Criptografia assimétrica: RSA, Diffie-Hellman e curvas elípticas - `vol03/cap018-criptografia-assimetrica-rsa-diffie-hellman-e.qmd`
- [x] **cap 019** - PKI, certificados digitais e cadeias de confiança - `vol03/cap019-pki-certificados-digitais-e-cadeias-de.qmd`
- [x] **cap 020** - TLS na prática: handshake, versões e configuração segura - `vol03/cap020-tls-na-pratica-handshake-versoes-e.qmd`
- [x] **cap 021** - Erros clássicos: criptografia mal empregada - `vol03/cap021-erros-classicos-criptografia-mal-empregada.qmd`

### Volume 4 — Identidade, Autenticação e Controle de Acesso

- [x] **cap 022** - Modelos de controle de acesso: DAC, MAC, RBAC e ABAC - `vol04/cap022-modelos-de-controle-de-acesso-dac-mac-rbac-e.qmd`
- [x] **cap 023** - Senhas: armazenamento, políticas e ataques - `vol04/cap023-senhas-armazenamento-politicas-e-ataques.qmd`
- [x] **cap 024** - Autenticação multifator e fatores de autenticação - `vol04/cap024-autenticacao-multifator-e-fatores-de.qmd`
- [x] **cap 025** - Federação de identidade: SAML, OAuth 2.0 e OpenID Connect - `vol04/cap025-federacao-de-identidade-saml-oauth-2-0-e.qmd`
- [x] **cap 026** - Gestão de identidades e de acessos privilegiados (IAM e PAM) - `vol04/cap026-gestao-de-identidades-e-de-acessos.qmd`
- [x] **cap 027** - Arquitetura Zero Trust - `vol04/cap027-arquitetura-zero-trust.qmd`

## Fase 2 — Segurança Aplicada


### Volume 5 — Segurança de Redes

- [x] **cap 028** - Arquitetura segura e segmentação de redes - `vol05/cap028-arquitetura-segura-e-segmentacao-de-redes.qmd`
- [x] **cap 029** - Firewalls: tipos, políticas e boas práticas - `vol05/cap029-firewalls-tipos-politicas-e-boas-praticas.qmd`
- [x] **cap 030** - VPNs: IPsec, WireGuard e acesso remoto seguro - `vol05/cap030-vpns-ipsec-wireguard-e-acesso-remoto-seguro.qmd`
- [x] **cap 031** - IDS, IPS e detecção em rede - `vol05/cap031-ids-ips-e-deteccao-em-rede.qmd`
- [x] **cap 032** - Segurança de DNS: ataques, DNSSEC e DoH - `vol05/cap032-seguranca-de-dns-ataques-dnssec-e-doh.qmd`
- [x] **cap 033** - Segurança do roteamento e BGP: sequestros, vazamentos e RPKI - `vol05/cap033-seguranca-do-roteamento-e-bgp-sequestros.qmd`
- [x] **cap 034** - Segurança em redes sem fio e enlaces de rádio - `vol05/cap034-seguranca-em-redes-sem-fio-e-enlaces-de-radio.qmd`
- [x] **cap 035** - Ataques de negação de serviço e estratégias de mitigação - `vol05/cap035-ataques-de-negacao-de-servico-e-estrategias.qmd`

### Volume 6 — Endpoints e Sistemas Operacionais

- [x] **cap 036** - Hardening de servidores Linux - `vol06/cap036-hardening-de-servidores-linux.qmd`
- [x] **cap 037** - Hardening de Windows e Active Directory - `vol06/cap037-hardening-de-windows-e-active-directory.qmd`
- [x] **cap 038** - Antivírus, EDR e XDR - `vol06/cap038-antivirus-edr-e-xdr.qmd`
- [x] **cap 039** - Gestão de vulnerabilidades e ciclo de patches - `vol06/cap039-gestao-de-vulnerabilidades-e-ciclo-de-patches.qmd`
- [x] **cap 040** - Segurança de dispositivos móveis e BYOD - `vol06/cap040-seguranca-de-dispositivos-moveis-e-byod.qmd`
- [x] **cap 041** - Criptografia de disco e proteção de dados em repouso - `vol06/cap041-criptografia-de-disco-e-protecao-de-dados-em.qmd`

### Volume 7 — Segurança de Aplicações

- [x] **cap 042** - Ciclo de desenvolvimento seguro e DevSecOps - `vol07/cap042-ciclo-de-desenvolvimento-seguro-e-devsecops.qmd`
- [x] **cap 043** - OWASP Top 10: panorama e como usar - `vol07/cap043-owasp-top-10-panorama-e-como-usar.qmd`
- [x] **cap 044** - Injeção: SQL, NoSQL e comandos de sistema - `vol07/cap044-injecao-sql-nosql-e-comandos-de-sistema.qmd`
- [x] **cap 045** - Cross-site scripting e ataques no lado do cliente - `vol07/cap045-cross-site-scripting-e-ataques-no-lado-do.qmd`
- [x] **cap 046** - Falhas de autenticação e gestão de sessão - `vol07/cap046-falhas-de-autenticacao-e-gestao-de-sessao.qmd`
- [x] **cap 047** - Falhas de controle de acesso: IDOR, SSRF e escalonamento - `vol07/cap047-falhas-de-controle-de-acesso-idor-ssrf-e.qmd`
- [x] **cap 048** - Segurança de APIs REST e GraphQL - `vol07/cap048-seguranca-de-apis-rest-e-graphql.qmd`
- [x] **cap 049** - SAST, DAST, SCA e automação de testes de segurança - `vol07/cap049-sast-dast-sca-e-automacao-de-testes-de.qmd`

### Volume 8 — Nuvem e Contêineres

- [x] **cap 050** - Modelo de responsabilidade compartilhada - `vol08/cap050-modelo-de-responsabilidade-compartilhada.qmd`
- [x] **cap 051** - IAM em nuvem e os erros de configuração mais caros - `vol08/cap051-iam-em-nuvem-e-os-erros-de-configuracao-mais.qmd`
- [x] **cap 052** - Segurança de contêineres e de imagens - `vol08/cap052-seguranca-de-conteineres-e-de-imagens.qmd`
- [x] **cap 053** - Segurança em Kubernetes - `vol08/cap053-seguranca-em-kubernetes.qmd`
- [x] **cap 054** - Infraestrutura como código e segurança de pipeline - `vol08/cap054-infraestrutura-como-codigo-e-seguranca-de.qmd`
- [x] **cap 055** - Segredos, cofres e gestão de chaves - `vol08/cap055-segredos-cofres-e-gestao-de-chaves.qmd`

## Fase 3 — Perspectiva Ofensiva


### Volume 9 — Testes de Invasão

- [x] **cap 056** - Metodologias e definição de escopo: PTES, OSSTMM e NIST SP 800-115 - `vol09/cap056-metodologias-e-definicao-de-escopo-ptes.qmd`
- [x] **cap 057** - Reconhecimento passivo e OSINT - `vol09/cap057-reconhecimento-passivo-e-osint.qmd`
- [x] **cap 058** - Varredura e enumeração - `vol09/cap058-varredura-e-enumeracao.qmd`
- [x] **cap 059** - Análise de vulnerabilidades - `vol09/cap059-analise-de-vulnerabilidades.qmd`
- [x] **cap 060** - Exploração: conceitos e anatomia de uma falha - `vol09/cap060-exploracao-conceitos-e-anatomia-de-uma-falha.qmd`
- [x] **cap 061** - Pós-exploração, persistência e movimentação lateral - `vol09/cap061-pos-exploracao-persistencia-e-movimentacao.qmd`
- [x] **cap 062** - Teste de invasão em aplicações web na prática - `vol09/cap062-teste-de-invasao-em-aplicacoes-web-na-pratica.qmd`
- [x] **cap 063** - Relatório técnico e comunicação de achados - `vol09/cap063-relatorio-tecnico-e-comunicacao-de-achados.qmd`

### Volume 10 — Fator Humano

- [x] **cap 064** - Engenharia social: os princípios psicológicos da persuasão - `vol10/cap064-engenharia-social-os-principios-psicologicos.qmd`
- [x] **cap 065** - Phishing, spear phishing e fraude do e-mail corporativo - `vol10/cap065-phishing-spear-phishing-e-fraude-do-e-mail.qmd`
- [x] **cap 066** - Fraudes digitais no Brasil: Pix, clonagem e golpes por mensageria - `vol10/cap066-fraudes-digitais-no-brasil-pix-clonagem-e.qmd`
- [x] **cap 067** - Segurança física e ataques presenciais - `vol10/cap067-seguranca-fisica-e-ataques-presenciais.qmd`
- [x] **cap 068** - Cultura de segurança e programas de conscientização - `vol10/cap068-cultura-de-seguranca-e-programas-de.qmd`

### Volume 11 — Malware e Inteligência de Ameaças

- [x] **cap 069** - Taxonomia de malware - `vol11/cap069-taxonomia-de-malware.qmd`
- [x] **cap 070** - Anatomia de um ataque de ransomware - `vol11/cap070-anatomia-de-um-ataque-de-ransomware.qmd`
- [x] **cap 071** - Análise estática em laboratório - `vol11/cap071-analise-estatica-em-laboratorio.qmd`
- [x] **cap 072** - Análise dinâmica e sandboxing - `vol11/cap072-analise-dinamica-e-sandboxing.qmd`
- [x] **cap 073** - MITRE ATT&CK e o mapeamento de TTPs - `vol11/cap073-mitre-att-ck-e-o-mapeamento-de-ttps.qmd`
- [x] **cap 074** - Inteligência de ameaças e indicadores de comprometimento - `vol11/cap074-inteligencia-de-ameacas-e-indicadores-de.qmd`

## Fase 4 — Perspectiva Defensiva


### Volume 12 — Blue Team, SOC e Detecção

- [x] **cap 075** - Estrutura e operação de um SOC - `vol12/cap075-estrutura-e-operacao-de-um-soc.qmd`
- [x] **cap 076** - Logging: o que registrar, por quanto tempo e por quê - `vol12/cap076-logging-o-que-registrar-por-quanto-tempo-e.qmd`
- [x] **cap 077** - SIEM: arquitetura, ingestão e correlação - `vol12/cap077-siem-arquitetura-ingestao-e-correlacao.qmd`
- [x] **cap 078** - Escrita de regras de detecção com Sigma e YARA - `vol12/cap078-escrita-de-regras-de-deteccao-com-sigma-e-yara.qmd`
- [x] **cap 079** - Threat hunting: caçando o que a regra não pegou - `vol12/cap079-threat-hunting-cacando-o-que-a-regra-nao-pegou.qmd`
- [x] **cap 080** - Deception: honeypots, honeytokens e canários - `vol12/cap080-deception-honeypots-honeytokens-e-canarios.qmd`
- [x] **cap 081** - Métricas e maturidade da detecção - `vol12/cap081-metricas-e-maturidade-da-deteccao.qmd`

### Volume 13 — Resposta a Incidentes e Forense Digital

- [x] **cap 082** - O ciclo de resposta a incidentes - `vol13/cap082-o-ciclo-de-resposta-a-incidentes.qmd`
- [x] **cap 083** - Preparação: plano, papéis e playbooks - `vol13/cap083-preparacao-plano-papeis-e-playbooks.qmd`
- [x] **cap 084** - Contenção, erradicação e recuperação - `vol13/cap084-contencao-erradicacao-e-recuperacao.qmd`
- [x] **cap 085** - Fundamentos de forense digital e cadeia de custódia - `vol13/cap085-fundamentos-de-forense-digital-e-cadeia-de.qmd`
- [x] **cap 086** - Forense de disco e sistemas de arquivos - `vol13/cap086-forense-de-disco-e-sistemas-de-arquivos.qmd`
- [x] **cap 087** - Forense de memória - `vol13/cap087-forense-de-memoria.qmd`
- [x] **cap 088** - Forense de rede e análise de tráfego - `vol13/cap088-forense-de-rede-e-analise-de-trafego.qmd`

### Volume 14 — Continuidade e Resiliência

- [x] **cap 089** - Backup: estratégias e a regra 3-2-1-1-0 - `vol14/cap089-backup-estrategias-e-a-regra-3-2-1-1-0.qmd`
- [ ] **cap 090** - Recuperação de desastres e continuidade de negócio - `vol14/cap090-recuperacao-de-desastres-e-continuidade-de.qmd`
- [ ] **cap 091** - Testes de continuidade e exercícios de mesa - `vol14/cap091-testes-de-continuidade-e-exercicios-de-mesa.qmd`
- [ ] **cap 092** - Alta disponibilidade e resiliência de infraestrutura - `vol14/cap092-alta-disponibilidade-e-resiliencia-de.qmd`
- [ ] **cap 093** - Recuperação após um ataque de ransomware - `vol14/cap093-recuperacao-apos-um-ataque-de-ransomware.qmd`

## Fase 5 — Governança e Fronteira


### Volume 15 — Governança, Risco e Conformidade

- [ ] **cap 094** - Governança de segurança e o papel do CISO - `vol15/cap094-governanca-de-seguranca-e-o-papel-do-ciso.qmd`
- [ ] **cap 095** - ISO/IEC 27001 e 27002 - `vol15/cap095-iso-iec-27001-e-27002.qmd`
- [ ] **cap 096** - NIST Cybersecurity Framework e CIS Controls - `vol15/cap096-nist-cybersecurity-framework-e-cis-controls.qmd`
- [ ] **cap 097** - LGPD na prática: bases legais, incidentes e a ANPD - `vol15/cap097-lgpd-na-pratica-bases-legais-incidentes-e-a.qmd`
- [ ] **cap 098** - Marco Civil, Lei 12.737 e o direito penal digital brasileiro - `vol15/cap098-marco-civil-lei-12-737-e-o-direito-penal.qmd`
- [ ] **cap 099** - Obrigações regulatórias de provedores de internet - `vol15/cap099-obrigacoes-regulatorias-de-provedores-de.qmd`
- [ ] **cap 100** - PCI-DSS e requisitos setoriais - `vol15/cap100-pci-dss-e-requisitos-setoriais.qmd`
- [ ] **cap 101** - Auditoria, conformidade e gestão de riscos de terceiros - `vol15/cap101-auditoria-conformidade-e-gestao-de-riscos-de.qmd`

### Volume 16 — Fronteira e Carreira

- [ ] **cap 102** - Segurança de sistemas de IA e modelos de linguagem - `vol16/cap102-seguranca-de-sistemas-de-ia-e-modelos-de.qmd`
- [ ] **cap 103** - Criptografia pós-quântica - `vol16/cap103-criptografia-pos-quantica.qmd`
- [ ] **cap 104** - Segurança de OT, IoT e sistemas embarcados - `vol16/cap104-seguranca-de-ot-iot-e-sistemas-embarcados.qmd`
- [ ] **cap 105** - Segurança da cadeia de suprimentos de software - `vol16/cap105-seguranca-da-cadeia-de-suprimentos-de-software.qmd`
- [ ] **cap 106** - Privacidade, anonimato e vigilância - `vol16/cap106-privacidade-anonimato-e-vigilancia.qmd`
- [ ] **cap 107** - Carreira, certificações e aprendizado contínuo - `vol16/cap107-carreira-certificacoes-e-aprendizado-continuo.qmd`

---

**Total:** 107 capitulos em 16 volumes (89 concluidos).

