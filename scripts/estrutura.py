"""
Fonte unica de verdade da estrutura do Manual de Seguranca da Informacao.

Gera:
  - o bloco `chapters:` do _quarto.yml
  - todos os stubs .qmd (regra stub-first)
  - o ROADMAP.md

Uso:
    python scripts/estrutura.py --stubs      # cria stubs faltantes
    python scripts/estrutura.py --quarto     # imprime o bloco chapters:
    python scripts/estrutura.py --roadmap    # regrava ROADMAP.md
    python scripts/estrutura.py --tudo
"""

import argparse
import os
import re
import unicodedata

# (fase, [(volume, titulo_volume, [titulos_capitulos])])
ESTRUTURA = [
    ("Fase 1 — Fundamentos", [
        ("Fundamentos da Segurança da Informação", [
            "O que é segurança da informação",
            "Os pilares: confidencialidade, integridade e disponibilidade",
            "Autenticidade, não repúdio e responsabilização",
            "Ativos, ameaças, vulnerabilidades e risco",
            "Modelagem de ameaças: STRIDE, árvores de ataque e abuse cases",
            "Gestão de risco: análise qualitativa e quantitativa",
            "Ética, legalidade e a fronteira do escopo autorizado",
        ]),
        ("Redes e Sistemas: a Base Técnica", [
            "A pilha TCP/IP sob a ótica do atacante e do defensor",
            "Endereçamento, roteamento e NAT",
            "Protocolos de aplicação e seus riscos: HTTP, DNS, SMTP e SNMP",
            "Fundamentos de sistemas operacionais: processos, permissões e memória",
            "Linux essencial para segurança",
            "Windows e Active Directory essencial",
            "Virtualização e montagem do laboratório de estudos",
        ]),
        ("Criptografia Aplicada", [
            "História e princípios da criptografia",
            "Criptografia simétrica: AES, modos de operação e AEAD",
            "Funções hash, HMAC e integridade",
            "Criptografia assimétrica: RSA, Diffie-Hellman e curvas elípticas",
            "PKI, certificados digitais e cadeias de confiança",
            "TLS na prática: handshake, versões e configuração segura",
            "Erros clássicos: criptografia mal empregada",
        ]),
        ("Identidade, Autenticação e Controle de Acesso", [
            "Modelos de controle de acesso: DAC, MAC, RBAC e ABAC",
            "Senhas: armazenamento, políticas e ataques",
            "Autenticação multifator e fatores de autenticação",
            "Federação de identidade: SAML, OAuth 2.0 e OpenID Connect",
            "Gestão de identidades e de acessos privilegiados (IAM e PAM)",
            "Arquitetura Zero Trust",
        ]),
    ]),
    ("Fase 2 — Segurança Aplicada", [
        ("Segurança de Redes", [
            "Arquitetura segura e segmentação de redes",
            "Firewalls: tipos, políticas e boas práticas",
            "VPNs: IPsec, WireGuard e acesso remoto seguro",
            "IDS, IPS e detecção em rede",
            "Segurança de DNS: ataques, DNSSEC e DoH",
            "Segurança do roteamento e BGP: sequestros, vazamentos e RPKI",
            "Segurança em redes sem fio e enlaces de rádio",
            "Ataques de negação de serviço e estratégias de mitigação",
        ]),
        ("Endpoints e Sistemas Operacionais", [
            "Hardening de servidores Linux",
            "Hardening de Windows e Active Directory",
            "Antivírus, EDR e XDR",
            "Gestão de vulnerabilidades e ciclo de patches",
            "Segurança de dispositivos móveis e BYOD",
            "Criptografia de disco e proteção de dados em repouso",
        ]),
        ("Segurança de Aplicações", [
            "Ciclo de desenvolvimento seguro e DevSecOps",
            "OWASP Top 10: panorama e como usar",
            "Injeção: SQL, NoSQL e comandos de sistema",
            "Cross-site scripting e ataques no lado do cliente",
            "Falhas de autenticação e gestão de sessão",
            "Falhas de controle de acesso: IDOR, SSRF e escalonamento",
            "Segurança de APIs REST e GraphQL",
            "SAST, DAST, SCA e automação de testes de segurança",
        ]),
        ("Nuvem e Contêineres", [
            "Modelo de responsabilidade compartilhada",
            "IAM em nuvem e os erros de configuração mais caros",
            "Segurança de contêineres e de imagens",
            "Segurança em Kubernetes",
            "Infraestrutura como código e segurança de pipeline",
            "Segredos, cofres e gestão de chaves",
        ]),
    ]),
    ("Fase 3 — Perspectiva Ofensiva", [
        ("Testes de Invasão", [
            "Metodologias e definição de escopo: PTES, OSSTMM e NIST SP 800-115",
            "Reconhecimento passivo e OSINT",
            "Varredura e enumeração",
            "Análise de vulnerabilidades",
            "Exploração: conceitos e anatomia de uma falha",
            "Pós-exploração, persistência e movimentação lateral",
            "Teste de invasão em aplicações web na prática",
            "Relatório técnico e comunicação de achados",
        ]),
        ("Fator Humano", [
            "Engenharia social: os princípios psicológicos da persuasão",
            "Phishing, spear phishing e fraude do e-mail corporativo",
            "Fraudes digitais no Brasil: Pix, clonagem e golpes por mensageria",
            "Segurança física e ataques presenciais",
            "Cultura de segurança e programas de conscientização",
        ]),
        ("Malware e Inteligência de Ameaças", [
            "Taxonomia de malware",
            "Anatomia de um ataque de ransomware",
            "Análise estática em laboratório",
            "Análise dinâmica e sandboxing",
            "MITRE ATT&CK e o mapeamento de TTPs",
            "Inteligência de ameaças e indicadores de comprometimento",
        ]),
    ]),
    ("Fase 4 — Perspectiva Defensiva", [
        ("Blue Team, SOC e Detecção", [
            "Estrutura e operação de um SOC",
            "Logging: o que registrar, por quanto tempo e por quê",
            "SIEM: arquitetura, ingestão e correlação",
            "Escrita de regras de detecção com Sigma e YARA",
            "Threat hunting: caçando o que a regra não pegou",
            "Deception: honeypots, honeytokens e canários",
            "Métricas e maturidade da detecção",
        ]),
        ("Resposta a Incidentes e Forense Digital", [
            "O ciclo de resposta a incidentes",
            "Preparação: plano, papéis e playbooks",
            "Contenção, erradicação e recuperação",
            "Fundamentos de forense digital e cadeia de custódia",
            "Forense de disco e sistemas de arquivos",
            "Forense de memória",
            "Forense de rede e análise de tráfego",
        ]),
        ("Continuidade e Resiliência", [
            "Backup: estratégias e a regra 3-2-1-1-0",
            "Recuperação de desastres e continuidade de negócio",
            "Testes de continuidade e exercícios de mesa",
            "Alta disponibilidade e resiliência de infraestrutura",
            "Recuperação após um ataque de ransomware",
        ]),
    ]),
    ("Fase 5 — Governança e Fronteira", [
        ("Governança, Risco e Conformidade", [
            "Governança de segurança e o papel do CISO",
            "ISO/IEC 27001 e 27002",
            "NIST Cybersecurity Framework e CIS Controls",
            "LGPD na prática: bases legais, incidentes e a ANPD",
            "Marco Civil, Lei 12.737 e o direito penal digital brasileiro",
            "Obrigações regulatórias de provedores de internet",
            "PCI-DSS e requisitos setoriais",
            "Auditoria, conformidade e gestão de riscos de terceiros",
        ]),
        ("Fronteira e Carreira", [
            "Segurança de sistemas de IA e modelos de linguagem",
            "Criptografia pós-quântica",
            "Segurança de OT, IoT e sistemas embarcados",
            "Segurança da cadeia de suprimentos de software",
            "Privacidade, anonimato e vigilância",
            "Carreira, certificações e aprendizado contínuo",
        ]),
    ]),
]

TITULOS_ACENTUADOS = {}  # preenchido em titulos.py se necessario


def slug(texto: str) -> str:
    t = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    t = t.lower()
    t = re.sub(r"[^a-z0-9]+", "-", t)
    t = re.sub(r"-+", "-", t).strip("-")
    if len(t) > 46:
        t = t[:46].rsplit("-", 1)[0]
    return t


def caminhos():
    """Retorna lista de (fase, num_vol, titulo_vol, num_cap, titulo_cap, path)."""
    out = []
    nvol = 0
    ncap = 0
    for fase, volumes in ESTRUTURA:
        for titulo_vol, capitulos in volumes:
            nvol += 1
            for titulo_cap in capitulos:
                ncap += 1
                path = f"vol{nvol:02d}/cap{ncap:03d}-{slug(titulo_cap)}.qmd"
                out.append((fase, nvol, titulo_vol, ncap, titulo_cap, path))
    return out


def gerar_stubs(raiz="."):
    criados = 0
    for _, _, _, ncap, titulo, path in caminhos():
        destino = os.path.join(raiz, path)
        os.makedirs(os.path.dirname(destino), exist_ok=True)
        if os.path.exists(destino):
            continue
        with open(destino, "w", encoding="utf-8") as f:
            f.write(f"# {titulo} {{#sec-cap{ncap:03d}}}\n\n*(em elaboracao)*\n")
        criados += 1
    print(f"stubs criados: {criados}")


def bloco_quarto():
    linhas = ["  chapters:", "    - index.qmd"]
    fase_atual = None
    nvol = 0
    for fase, vol, titulo_vol, _, _, path in caminhos():
        if fase != fase_atual:
            fase_atual = fase
            linhas.append(f"    # ===== {fase} =====")
        if vol != nvol:
            nvol = vol
            linhas.append("    - part: |")
            linhas.append(f"        Volume {vol} — {titulo_vol}")
            linhas.append("      chapters:")
        linhas.append(f"        - {path}")
    linhas.append("    - referencias.qmd")
    return "\n".join(linhas)


def status_atuais(raiz="."):
    """Le o ROADMAP.md existente e devolve {num_cap: marcador}.

    Sem isso, regravar o ROADMAP zeraria todo capitulo ja concluido -- o
    arquivo e a fila autoritativa de producao, nao um artefato descartavel.
    """
    destino = os.path.join(raiz, "ROADMAP.md")
    if not os.path.exists(destino):
        return {}
    with open(destino, encoding="utf-8") as f:
        conteudo = f.read()
    achados = re.findall(r"^- \[([ x~])\] \*\*cap (\d{3})\*\*", conteudo, re.M)
    return {int(num): marca for marca, num in achados}


def gerar_roadmap(raiz="."):
    status = status_atuais(raiz)
    L = ["# ROADMAP — Manual de Seguranca da Informacao", "",
         "Fila autoritativa de producao. Status: `[ ]` pendente | `[~]` em andamento | `[x]` concluido.",
         "", "Commit por capitulo: `cap NNN: <titulo>` com o status atualizado no mesmo commit.", ""]
    fase_atual = None
    nvol = 0
    for fase, vol, titulo_vol, ncap, titulo, path in caminhos():
        if fase != fase_atual:
            fase_atual = fase
            L += ["", f"## {fase}", ""]
        if vol != nvol:
            nvol = vol
            L += ["", f"### Volume {vol} — {titulo_vol}", ""]
        marca = status.get(ncap, " ")
        L.append(f"- [{marca}] **cap {ncap:03d}** - {titulo} - `{path}`")
    total = len(caminhos())
    concluidos = sum(1 for m in status.values() if m == "x")
    L += ["", "---", "",
          f"**Total:** {total} capitulos em {nvol} volumes "
          f"({concluidos} concluidos).", ""]
    with open(os.path.join(raiz, "ROADMAP.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")
    print(f"ROADMAP.md gravado ({total} capitulos, "
          f"{concluidos} concluidos preservados)")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--stubs", action="store_true")
    p.add_argument("--quarto", action="store_true")
    p.add_argument("--roadmap", action="store_true")
    p.add_argument("--tudo", action="store_true")
    a = p.parse_args()
    if a.tudo or a.stubs:
        gerar_stubs()
    if a.tudo or a.roadmap:
        gerar_roadmap()
    if a.quarto:
        print(bloco_quarto())
    if not any([a.stubs, a.quarto, a.roadmap, a.tudo]):
        c = caminhos()
        print(f"{len(c)} capitulos, {c[-1][1]} volumes")
