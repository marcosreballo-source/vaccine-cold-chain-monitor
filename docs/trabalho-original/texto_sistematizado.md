> Versão final entregue do trabalho de **SSC0530 – Introdução a Sistemas de Informação** (ICMC/USP, 1º semestre de 2025), exportada do Google Docs do grupo (última edição em 23/06/2025). Texto mantido como entregue; é a base do problema e da especificação que este repositório implementa. O PDF entregue está em [`texto_sistematizado.pdf`](texto_sistematizado.pdf).

**UNIVERSIDADE DE SÃO PAULO**  
**INSTITUTO DE CIÊNCIAS MATEMÁTICAS E DE COMPUTAÇÃO**

# **SSC0530 \- Introdução a Sistemas de Informação**

## **SMARTHEALTH SOLUTIONS LTDA**

**\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**

**PROPOSTA TÉCNICA PARA GESTÃO INTELIGENTE DE ENERGIA E ÁGUA EM UNIDADES BÁSICAS DE SAÚDE**

**\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**

**Discentes:**  
Arthur Gagliardi Azorli NºUSP 16855452  
Marcos Vinicius Reballo NºUSP 7576746  
Mateus Saracuza NºUSP 13674087  
Nícolas Silva Scorza NºUSP 17025079  
Pedro dos Santos Kemp  NºUSP 17064431

## 

**São Carlos \- SP**  
2025  

## **Resumo Executivo**

Este trabalho propõe um sistema de Informação inovador, baseado em Internet das Coisas (IoT), para otimizar o consumo energético e monitorar a conservação de vacinas em 11 Unidades Básicas de Saúde (UBS) de São Carlos. A iniciativa visa retomar e aprimorar o sistema de monitoramento da UFSCar, descontinuado após a pandemia de COVID-19, adicionando gestão energética sustentável e controle automatizado de inventário farmacêutico. A solução integra sensores IoT, análise de dados em tempo real e interfaces intuitivas para aumentar a eficiência operacional, reduzir custos energéticos e garantir a qualidade dos imunobiológicos, contribuindo para a sustentabilidade e modernização do sistema de controle e administração de vacinas.

**1\. INTRODUÇÃO**

**1.1 Contextualização do problema**

O Sistema Único de Saúde (SUS) brasileiro enfrenta crescentes desafios relacionados à sustentabilidade energética e à preservação adequada de medicamentos e vacinas. Dados oficiais do Tribunal de Contas da União (TCU) revelam que o Brasil desperdiçou mais de 28 milhões de doses de vacinas que perderam a validade, resultando em prejuízo de R\$1,2 bilhão apenas entre 2021 e 2022 \[1\]\[2\]. Este problema evidencia falhas críticas nos sistemas de monitoramento e conservação de imunobiológicos nas unidades de saúde pública.

No contexto das UBS, dois problemas críticos convergem: o alto consumo energético desnecessário e as perdas significativas de imunobiológicos por falhas no controle de temperatura. A ANVISA estabelece que as vacinas devem ser mantidas rigorosamente entre \+2°C e \+8°C, conforme a RDC 430/2020, para preservar sua eficácia e segurança \[3\]. Contudo, o monitoramento manual de temperatura de refrigeradores de vacinas ainda é realizado três vezes ao dia por funcionários, representando um processo ineficiente e suscetível a falhas humanas(verificado por membros em entrevista com responsáveis de uma unidade).

Em São Carlos, interior do estado de São Paulo, essa problemática se manifesta de forma particularmente evidente nas 11 UBS do município \[4\], onde a demanda por soluções inovadoras é crescente. Durante a pandemia de COVID-19, a Universidade Federal de São Carlos (UFSCar) desenvolveu um sistema pioneiro de monitoramento de temperatura para preservação de vacinas no município. O sistema utilizava dispositivos IoT com termômetros eletrônicos que coletavam dados a cada cinco segundos, transmitindo informações via internet para o Data Center da universidade e emitindo alertas em tempo real quando a temperatura ultrapassasse os limites seguros \[5\]. Embora tecnicamente bem-sucedida, essa iniciativa foi descontinuada após o período pandêmico, deixando as UBS novamente dependentes de processos manuais inadequados.

O tema escolhido pelo grupo, Gestão Inteligente de Energia e Água, representa uma das oportunidades de modernização no setor público de saúde. A problemática exposta acima escolhida para nossa proposta, encontra no setor de saúde pública um campo fértil para inovações tecnológicas, especialmente através da coleta de dados via sensores IoT, gerando alertas sobre desperdícios de energia, identificando padrões de consumo e controlando perdas de insumos por expiração ou acondicionamento inadequado.

**1.2 Motivação e justificativa**

A motivação para desenvolvimento desta solução fundamenta-se em evidências científicas que demonstram a criticidade do problema e o potencial transformador de soluções tecnológicas. Estudos da região de São José do Rio Preto, publicados na SciELO, confirmam que 41,4% das doses de vacinas do estudo, que sofreram alteração de temperatura, foram perdidas, sendo 70,1% das falhas causadas por problemas estruturais em refrigeradores \[6\]. Estas estatísticas realizadas e validadas evidenciam a necessidade urgente de sistemas de monitoramento contínuo e automatizado.

Do ponto de vista energético, estabelecimentos de saúde apresentam características que tornam essencial a implementação de soluções de gestão inteligente. Dados do Conselho Brasileiro de Construção Sustentável indicam consumo energético entre 73,93 e 107,50 kWh/m²/ano em UBS \[7\], representando oportunidade significativa de otimização. Projetos da ANEEL em hospitais de Salvador e Recife comprovaram economias de até 30% no consumo energético  geral dos estabelecimentos\[8\], evidenciando o potencial de economia através de monitoramento inteligente.

A proposta de solução consiste em um Sistema de Informação integrado que combina monitoramento IoT de temperatura e umidade, gestão inteligente do consumo energético, controle automatizado de inventário de vacinas e interface web responsiva para gestão centralizada. O sistema permitirá monitoramento em tempo real de todas as UBS do município, emissão de alertas preventivos, geração de relatórios de conformidade regulatória e otimização automática do consumo energético através de algoritmos de machine learning.

Estima-se que o investimento inicial seja de aproximadamente R\$35.501,40, para as 11 UBS de São Carlos. Acreditamos que o retorno do investimento ocorrerá em aproximadamente 10 meses, considerando uma economia energética de 10-20%, visto que a validação pela ANEEL \[8\] foi realizada em todo o sistema energético dos hospitais e não somente no setor de refrigeração. Ainda, o ROI calculado se baseia também na redução de perdas de vacinas e melhor controle de inventário, além do aumento da eficiência da equipe responsável. Estes benefícios tangíveis, aliados à melhoria na qualidade dos serviços de saúde e à conformidade regulatória, justificam plenamente o desenvolvimento da nossa solução proposta.

**1.3 Soluções existentes**

O mercado atual apresenta diversas soluções tecnológicas para monitoramento de temperatura e gestão energética em estabelecimentos de saúde, cada uma com características específicas que podem ser analisadas comparativamente à proposta apresentada.

Na área de monitoramento de temperatura para conservação de medicamentos, empresas como a Sensorweb oferecem soluções IoT especializadas para cadeia de frio farmacêutica. Suas tecnologias incluem sensores de temperatura e umidade conectados via internet, dashboards para visualização de dados e sistema de alertas por email e SMS \[9\]. Essas soluções, embora tecnicamente robustas, focam exclusivamente no aspecto de conservação, não integrando funcionalidades de gestão energética, otimização de processos operacionais ou controle de inventário integrado.

Na cidade de Lages-SC, por exemplo, foi implementado um sistema de monitoramento online baseado em IoT para câmaras frias em UBS, desenvolvido pela startup Circuits \[10\]. Este sistema utiliza sensores que verificam a temperatura a cada 5 minutos e enviam notificações via dispositivos móveis. Esse caso em específico demonstra a viabilidade de soluções similares em um contexto municipal.

No setor de gestão energética, a EDP (concessionária de energia da região sul) concluiu um projeto de eficiência energética em toda rede elétrica do Pronto Atendimento de Poá, com investimento de R\$682 mil, resultando em economia anual de R\$120 mil \[11\]. Outro exemplo, o Hospital Regional de Patos foi contemplado com um projeto da Energisa avaliado em R\$299,4 mil, com a meta de reduzir o consumo de 359,27 para 245,71 MWh/ano \[12\]. Tais soluções focam principalmente em aspectos comerciais e de infraestrutura dos estabelecimentos. Contudo esses projetos, apesar do maior escopo/investimento, não oferecem a integração com sistemas de monitoramento operacional.

O diferencial da solução proposta reside na integração inédita de múltiplas funcionalidades em uma única plataforma: monitoramento de temperatura, gestão energética inteligente, controle de inventário automatizado e interface unificada para gestão municipal. Enquanto soluções existentes abordam aspectos isolados do problema, nossa proposta oferece uma visão holística que combina sustentabilidade, eficiência operacional e conformidade regulatória em um sistema específico para o contexto das UBS brasileiras. Além disso, o formato da nossa solução permite que tais funcionalidades de eficiência energética possam ser agregadas futuramente, incluindo controle e otimização de sistemas de calefação ou demais sistemas energéticos e de hidráulica da UBS.

**2\. A SOLUÇÃO PROPOSTA**

**2.1 Funcionalidades**

O sistema proposto integra funcionalidades abrangentes organizadas em módulos interconectados que atendem às necessidades específicas de gestão sustentável das UBS. O sistema SmartHealth IOT-UBS apresenta as seguintes funcionalidades principais:

1. **Módulo de Monitoramento:** Interface dashboard com lista de *cards* representando cada UBS, equipados com barra de pesquisa e filtros avançados. Cada card exibe identificação da instituição, indicadores de temperatura (máxima, mínima e média), status de comunicação (online/offline) e nível de risco para conservação de vacinas, com sistema de priorização automática que eleva cards com problemas para o topo da lista.  
2. **Monitoramento em Tempo Real:** A funcionalidade de monitoramento em tempo real constitui o núcleo tecnológico da solução, utilizando sensores IoT para coleta contínua de dados de temperatura, umidade e consumo energético. O sistema processa essas informações através de algoritmos de análise que identificam padrões anômalos, tendências de consumo e situações de risco iminente. Alertas automatizados são enviados via múltiplos canais (email, SMS, push notifications) quando parâmetros críticos são violados, incluindo estimativas de tempo restante para resolução antes que vacinas sejam comprometidas.  
3. **Relatórios Automatizados:** O módulo de relatórios oferece visualizações gráficas e textuais customizáveis por período (diário, semanal, mensal, anual), permitindo análise histórica independente da data atual. Relatórios incluem métricas de conformidade regulatória ANVISA \[13\], indicadores de eficiência energética, custos operacionais e projeções de economia.  
4. **Gestão de Inventário:** A funcionalidade de gestão de inventário automatizada utiliza sistemas de código de barras para monitoramento do estoque de vacinas, com controle de validade e alertas preventivos de vencimento.  
5. **Comunicação Integrada:** O sistema incorpora funcionalidades de comunicação integrada entre administradores municipais e gestores das UBS, permitindo registro de ocorrências, solicitação de suporte técnico e compartilhamento de relatórios.

**2.2 Questões técnicas**

A infraestrutura técnica da solução baseia-se em arquitetura distribuída utilizando tecnologias de Internet das Coisas (IoT) para coleta de dados, computação em nuvem para processamento e análise, e aplicações web responsivas para interface de usuário.

Addendo: ESP32-WROOM-32 foi escolhido devido ao custo/benefício inicial para Prova de Conceito, seus pontos ruins consistem principalmente por armazenamento em memória física e RAM(*Nota Responsável Embarcados*)

**Infraestrutura de Hardware:**

| Componente | Especificações | Fonte | Custo/Unidade |
| :---- | :---- | :---- | :---- |
| ESP32-WROOM-32 | Dual-core 240MHz, WiFi/Bluetooth, 4MB Flash | [MercadoLivre](https://www.mercadolivre.com.br/esp32-doit-devkit-com-esp32-wroom-32/p/MLB28251016) | R\$ 49,90 |
| DHT22 | ±0.5°C, 0-100% UR, 2s sampling | [Eletrogate](https://www.eletrogate.com/sensor-de-umidade-e-temperatura-dht22-am2302) | R\$ 35,50 |
| DS18B20 | \-55°C a \+125°C, IP68 | [MercadoLivre](https://produto.mercadolivre.com.br/MLB-1815340875-sensor-de-temperatura-ds18b20-a-prova-dagua-arduino-_JM) | R\$ 11,90 |
| SCT-013 | Medidor de corrente não invasivo, 30A | [Eletrogate](https://www.eletrogate.com/sensor-de-corrente-nao-invasivo-30a-sct-013) | R\$ 42,00 |
| Gabinete | IP65, instalação e cabeamento | \- | R\$ 120,00 |

**Custo total por UBS:** R\$ 259,30

**Arquitetura de Software(IoT):**

Sistema operacional escolhido foi Linux com restrição de arquivos maiores (para embarcados):

* **C++ (Backend):** Permitindo uma maior velocidade na resposta de eventos e captura de estados do ambiente interno e externo, além de sua programação de fácil modularização, fácil manipulação de dados binários, pouco consumo de memória e energia, portabilidade com diferentes arquiteturas e sistemas operacionais, fácil implementação, orientação a objeto com herança múltipla, programação multi-nivelada (Alto e baixo Nível), programação assíncrona, bibliotecas consolidadas, amplo suporte a ferramentas e comunidade.\[26\] 

* **SQLite  (Dados Estruturados):** SQLite ocupa pouco espaço de memória, correspondendo melhor ao armazenamento limitado do microcontrolador e fornece um meio simplificado para salvar informações que o programa possa necessitar (como a identificação do dispositivo, da UBS, e dados para Warm Boot);\[27\]

* **MQTT (Comunicação):** Protocolo padrão de mercado para IoT, com baixa latência (≤100ms), baixo consumo de banda e suporte a TLS 1.3 para segurança em transmissões críticas \[14\].

**Arquitetura de Software:**

A escolha tecnológica foi fundamentada em requisitos específicos de sistemas para saúde:

* **Node.js (Backend):** Selecionado por sua alta eficiência em I/O assíncrono, capacidade de lidar com até 1.000 conexões simultâneas e ampla biblioteca de módulos para sistemas IoT \[15\].

* **PostgreSQL (Dados Estruturados):** Escolhido pelo suporte nativo a JSON para armazenamento eficiente de dados de sensores em formato semi-estruturado, além de robustas capacidades de consulta e indexação \[16\].

* **InfluxDB (Séries Temporais):** Database especializada em dados de séries temporais, otimizada para dados de sensores com alta frequência de coleta, oferecendo compressão eficiente e consultas rápidas para análise de tendências \[17\].

* **React.js (Frontend):** Framework para desenvolvimento de interfaces responsivas com atualizações em tempo real, componentes reutilizáveis e desempenho otimizado para dashboards de monitoramento \[18\].

**Infraestrutura de Nuvem:**

| Serviço | Especificação | Custo Mensal | Justificativa |
| :---- | :---- | :---- | :---- |
| AWS IoT Core | 50 dispositivos, 300 msg/dispositivo/dia | R\$ 150,00 | Garantia de entrega de alertas 24/7 via WAN |
| EC2 t3.micro | 2vCPU, 1GB RAM, Linux | R\$ 150,00 | Processamento modelos LSTM-ARIMA |
| S3 Standard | 50GB armazenamento | R\$ 87,50 | Histórico regulatório ANVISA (5 anos) |

**Custo Cloud Total Estimado:** R\$ 387,50/mês para 11 UBS

A infraestrutura em nuvem é essencial para garantir que os gestores possam ser avisados a qualquer momento sobre situações críticas. O ambiente WAN (Wide Area Network) necessita de uma infraestrutura intermediária confiável para garantir a entrega de mensagens críticas mesmo quando os dispositivos móveis dos gestores estão em redes diferentes ou temporariamente indisponíveis \[19\]. Adicionalmente, o processamento de modelos de machine learning requer recursos computacionais além da capacidade dos dispositivos IoT locais.

**Integração com Sistemas de Saúde:**

A solução implementa integração com sistemas legados seguindo as diretrizes da Rede Nacional de Dados em Saúde (RNDS) \[20\]:

1. **Padrões RNDS implementados:**

   * Utilização de APIs REST com autenticação OAuth 2.0

   * Certificação Digital ICP-Brasil para dispositivos

   * Criptografia TLS 1.3 para transmissão de dados

   * Conformidade com Lei Geral de Proteção de Dados (LGPD)

2. **Compatibilidade com padrões HL7 FHIR:**

   * FHIR Release 4.0.1 (padrão atual do DATASUS)

   * Recursos FHIR implementados:

     * Observation: Registros de temperatura/umidade;

     * Device: Metadados dos sensores;

     * Location: Localização das UBS;

     * Organization: Estrutura organizacional do município;

   * Perfil Brasileiro de Implementação (Brasil Core);

Esta integração assegura interoperabilidade com sistemas municipais existentes e prontuários eletrônicos, permitindo fluxo automatizado de informações sobre conservação de vacinas e consumo energético.

**2.3 Questões organizacionais**

A implementação da solução demanda transformações organizacionais nas UBS participantes, exigindo recursos humanos, financeiros e estruturais específicos.

**Recursos Necessários:**

| Recurso | Descrição | Justificativa |
| :---- | :---- | :---- |
| Conectividade | Internet banda larga mínima 5 Mbps | Transmissão de dados em tempo real |
| Infraestrutura elétrica | Pontos de energia estabilizada | Funcionamento contínuo dos sensores |
| Equipe técnica | Responsável técnico por UBS | Manutenção básica e primeiro atendimento |
| Permissões | Acesso aos refrigeradores | Instalação e manutenção dos sensores |

**Investimento Inicial Detalhado:**

| Item | Quantidade | Valor Unitário (R\$) | Total (R\$) |
| :---- | :---- | :---- | :---- |
| Hardware por UBS | 11 | 259,30 | 2.852,30 |
| Infraestrutura Cloud (12 meses) | 12 | 387,50 | 4.650,00 |
| Desenvolvimento do software | 1 | 20.000,00 | 20.000,00 |
| Treinamento de equipes | 11 | 299,00 | 3.289,00 |
| Implementação e configuração | 11 | 428,73 | 4.716,10 |
| **Total** |  |  | **35.501,40** |

**Mudanças Culturais:**

A implementação requer transição de processos manuais para digitais, aceitação de monitoramento automatizado e desenvolvimento de rotinas de resposta a alertas eletrônicos. A complexidade dessas mudanças é considerada moderada, dado que profissionais de saúde utilizam tecnologias digitais em suas atividades diárias, em paralelo com processos e sistemas legado/analógicos. Logo, acreditamos que será necessário um período de adaptação de 3-6 meses com suporte técnico intensivo.

A gestão da mudança organizacional poderá seguir uma metodologia estruturada que inclua:

1. Comunicação prévia sobre os benefícios da solução;

2. Envolvimento de lideranças locais (conselhos de bairro, síndicos, moradores dos arredores) no processo de implementação;

3. Treinamento escalonado por grupos de funcionários(gestores, enfermeiros, secretariado, almoxarifado);

4. Estabelecimento de canais de feedback contínuo;

Indicadores de sucesso propostos da mudança incluirão a taxa de adoção do sistema, redução de registros manuais de temperatura e melhoria nos índices de conformidade regulatória.

**2.4 Questões humanas**

O impacto da solução nos funcionários das UBS será majoritariamente positivo, proporcionando redução de tarefas repetitivas, melhoria na qualidade do trabalho e maior segurança na conservação de vacinas. Os profissionais de enfermagem, atualmente responsáveis pelo controle manual de temperatura, terão esse tempo liberado para atividades de maior valor agregado no atendimento aos pacientes. A automatização do processo reduzirá o estresse associado à responsabilidade de controle manual e possíveis perdas de medicamentos.

Gestores das UBS serão diretamente beneficiados pela visibilidade em tempo real de indicadores operacionais, relatórios automatizados para auditorias e alertas preventivos que permitem ação proativa antes da ocorrência de problemas críticos. O sistema fornecerá informações gerenciais que facilitarão tomada de decisões baseadas em dados e planejamento de recursos mais eficiente. O controle de inventário em tempo real reduzirá desperdícios e perdas das vacinas, além da diminuição de estoques desnecessários no longo prazo. 

A capacitação de recursos humanos seguirá programa estruturado incluindo:

* Treinamento inicial de 8 horas para operadores básicos;

* 16 horas para administradores locais;

* 24 horas para gestores municipais;

O conteúdo abrangerá operação da interface web, interpretação de alertas, procedimentos de resposta a emergências e geração de relatórios. Material de apoio incluirá manuais ilustrados, vídeos tutoriais e sistema de help desk para suporte contínuo.

A resistência à mudança será minimizada através de estratégias de engajamento incluindo demonstrações práticas dos benefícios, depoimentos de funcionários da unidade pioneira e reconhecimento de funcionários que se destacarem na adoção da nova tecnologia. Canais de comunicação bidirecional devem permitir a coleta de sugestões de melhorias e adaptações do sistema às necessidades específicas de cada unidade, quando houver.

**2.5 Processos de negócio**

A implementação da solução transformará fundamentalmente os processos de negócio relacionados à conservação de vacinas e gestão energética nas UBS. O processo atual de controle de temperatura em planilhas impressas será substituído por monitoramento contínuo automatizado com registro digital em tempo real. Esta mudança eliminará possibilidades de erro humano, gaps de monitoramento durante finais de semana e feriados, e fornecerá rastreabilidade completa para eventuais auditorias regulatórias.

**Processos Alterados:**

1. **Controle de Temperatura:**

   * **Antes:** Verificação manual 3x/dia (manhã/tarde/noite);

   * **Depois:** Monitoramento automatizado 24/7 com alertas imediatos;

   * **Benefícios:** Redução estimada de 80% no tempo gasto, precisão aumentada em 95%;

2. **Gestão de Inventário:**

   * **Antes:** Contagem manual semanal, registro em planilhas digitais/impressas;

   * **Depois:** Controle automatizado em tempo real, alertas de vencimento;

   * **Benefícios:** Redução de perdas por vencimento, planejamento otimizado;

3. **Manutenção de Equipamentos:**

   * **Antes:** Corretiva após falhas;

   * **Depois:** Preventiva baseada em análise preditiva;

   * **Benefícios:** Aumento na vida útil dos refrigeradores;

**Novos Processos Criados:**

1. **Gestão Energética Inteligente:**

   * Análise de padrões de consumo;

   * Identificação de oportunidades de economia;

   * Otimização automática de operação de equipamentos;

   * Benefícios: Redução de até 20% no consumo energético;

2. **Resposta a Alertas Críticos:**

   * Procedimento padronizado para cada tipo de alerta;

   * Escalabilidade de notificações conforme gravidade;

   * Registro de ações tomadas para auditoria;

   * Benefícios: Tempo de resposta reduzido drasticamente;

3. **Análise de Desempenho Energético:**

   * Benchmarking entre UBS;

   * Relatórios de sustentabilidade periódicos;

   * Definição de metas de redução específicas;

   * Benefícios: Competição saudável entre unidades, reconhecimento público;

A transformação destes processos resultará em economia de recursos, maior segurança na conservação de imunobiológicos e sustentabilidade ambiental, alinhando-se assim aos objetivos estratégicos do SUS e às metas de desenvolvimento sustentável.

**3\. PROCESSAMENTO DA INFORMAÇÃO**

**3.1 Dados de entrada**

O sistema processa múltiplas categorias de dados coletados continuamente através de sensores IoT distribuídos nas UBS e interfaces de usuário web. Os dados primários incluem:

**Dados de Sensores Físicos:**

* **Temperatura:** Medições internas dos refrigeradores (DS18B20, ±0.5°C, intervalo: 30s);

* **Temperatura ambiente:** Condições do entorno dos equipamentos (DHT22, intervalo: 3min);

* **Umidade relativa:** Medição do ar ambiente (DHT22, ±2%, intervalo: 3 min);

* **Consumo energético:** Corrente elétrica, tensão, potência ativa/reativa (SCT-013, intervalo: 1 min);

* **Status de porta:** Sensores magnéticos[^1] para detecção de abertura (intervalo: evento);

**Dados de Inventário:**

* Registro de entrada/saída de vacinas (código de barras/interface manual);

* Datas de fabricação e validade dos imunobiológicos;

* Lotes e fabricantes;

* Requisitos específicos de armazenamento por tipo de vacina;

**Dados Contextuais:**

* Geolocalização GPS das UBS;

* Horários de funcionamento e fluxo de atendimento;

* Histórico de manutenções dos equipamentos de refrigeração;

**Dados Administrativos:**

* Cadastro de funcionários e *feature flags*;

* Configurações de alertas personalizadas por unidade;

* Registros de ações tomadas em resposta a alertas;

* Feedbacks dos funcionários sobre a plataforma;

A combinação destes dados permite análises abrangentes que vão além do simples monitoramento, possibilitando correlações entre condições ambientais, padrões de uso e eficiência energética dos equipamentos.

**3.2 Processamento**

O processamento dos dados segue arquitetura de pipeline distribuído utilizando tecnologias de streaming analytics para análise em tempo real e batch processing para análises históricas complexas.

**Pipeline de Processamento com modelos de Machine Learning:**

1. **Validação e Filtragem:**

   * Eliminação de outliers e valores inconsistentes;

   * Interpolação de dados faltantes quando aplicável;

   * Normalização de escalas e padronização de formatos;

2. **Detecção de Anomalias:**

   * **Modelos LSTM-ARIMA Híbridos;**

   * Justificativa técnica: A combinação de Long Short-Term Memory (LSTM) e modelos Auto-Regressive Integrated Moving Average (ARIMA) oferece performance superior em séries temporais de temperatura e energia \[21\]. ARIMA captura padrões sazonais com alta precisão (CV-RMSE ≤2,93%), enquanto LSTM identifica não-linearidades complexas e relacionamentos de longo prazo (MAPE ≤7,2%) \[22\].

   * Implementação: Ponderação residual combinando predições de ambos os modelos, utilizando *ensemble learning;*

3. **Clusterização para Personalização dos padrões de consumo/fluxo de compras:**

   * **Algoritmo K-Means;**

   * Justificativa técnica: A clusterização permite identificar grupos de UBS com comportamentos similares, possibilitando políticas personalizadas mais eficientes \[23\]. K-Means foi selecionado por sua eficiência computacional e facilidade de interpretação, crucial para a explicabilidade em sistemas de saúde pública.

   * Features utilizadas:

     * Localização geográfica (influencia condições climáticas);

     * Idade dos refrigeradores (afeta eficiência energética);

     * Padrão histórico de consumo (kWh/m²);

     * Variação média de temperatura;

     * Fluxo de insumos imunobiológicos;

   * Resultado: Criação de clusters distintos para personalização de políticas energéticas e de compras, de estoque e alertas:

     * UBS Urbanas: Alto fluxo de pacientes, prioridade em alertas imediatos, manutenção de estoque;

     * UBS Rurais: Variação térmica acentuada, ênfase em resiliência energética, estoques *on-demand;*

     * UBS Especiais: Vacinas termolábeis, tolerância ≤0,5°C;

4. **Análise Preditiva:**

   * Previsão de falhas em equipamentos;

   * Estimativa de economia energética potencial;

   * Projeção de demanda de vacinas;

   * Recomendações de manutenção preventiva;

A arquitetura de processamento é escalável, permitindo adaptação conforme o crescimento do número de UBS atendidas ou a inclusão de novos tipos de sensores ou sistemas de agregados ao SI proposto. O sistema implementa processamento edge nos dispositivos ESP32 para redução de tráfego de dados e resiliência em caso de falhas de conectividade temporárias.

**3.3 Dados de saída**

Os dados de saída do sistema são apresentados através de múltiplas interfaces adaptadas às necessidades específicas dos diferentes perfis de funcionários, transformando dados brutos em informações acionáveis e acessíveis.

**Relatórios Automatizados:**

| Tipo | Periodicidade | Conteúdo | Destinatário |
| :---- | :---- | :---- | :---- |
| Técnico | Diário | Dados brutos dos sensores, status de conexão, calibragem | Equipe TI |
| Operacional | Semanal | Desvios de temperatura, consumo energético, incidentes, estoque de insumos | Gestor UBS |
| Regulatório | Mensal | Conformidade com ANVISA RDC 430/2020, evidências de infrações | Vigilância Sanitária |
| Estratégico | Trimestral | ROI, redução de emissões CO₂, economia acumulada, recomendações de compra | Secretaria Municipal |

Os relatórios são gerados em formatos adaptáveis (PDF, Excel, CSV) e podem ser customizados conforme necessidades específicas de cada unidade ou gestor.

**Alertas Contextualizados:**

O sistema gera alertas inteligentes que incluem:

* Identificação precisa do problema;

* Análise de impacto (vacinas afetadas, prazo estimado para degradação);

* Recomendações de ação baseadas em histórico;

* Escalonamento automático conforme criticidade;

Os dados de saída são projetados para impactar positivamente múltiplos stakeholders:

* **Técnicos de enfermagem:** Redução de trabalho manual, maior segurança;

* **Gestores de UBS:** Tomada de decisão baseada em dados, resposta proativa;

* **Secretaria Municipal:** Otimização de recursos, planejamento estratégico;

* **Pacientes:** Maior segurança na eficácia de vacinas, melhor atendimento;

**4\. CONCORRÊNCIA E VANTAGEM COMPETITIVA**

**4.1 Modelo de Forças Competitivas de Porter**

A análise do ambiente competitivo utilizando o modelo de Porter revela um cenário complexo onde diferentes forças influenciam a viabilidade e sustentabilidade da solução proposta no mercado de soluções tecnológicas para saúde pública. Consideramos nossa empresa em uma disputa licitatória inicial ou uma de manutenção/atualização dos serviços oferecidos ao Poder Público.

**Rivalidade entre Concorrentes Existentes (Intensidade: Moderada)**

O mercado de soluções IoT para saúde apresenta players estabelecidos como Sensorweb (sistemas de monitoramento térmico \- sensorweb.com.br) e Nexxto (gestão de cadeia frio \- nexxto.com). Essas empresas oferecem soluções parciais, focadas principalmente no monitoramento de temperatura. A concorrência é mitigada pelos seguintes fatores:

* Soluções existentes atendem apenas parcialmente as necessidades (monitoramento ou gestão energética, raramente ambos e sem controle de estoque);

* Poucas soluções são especificamente desenhadas para o contexto específico do SUS;

* Diferenciação técnica através de integração RNDS via FHIR, exigida para sistemas públicos de saúde \[20\];

Nossa solução apresenta três diferenciais competitivos principais:

1. Integração HL7 FHIR com RNDS (conformidade com requisitos do SUS);

2. Algoritmos de otimização energética/controle de estoque baseados em LSTM-ARIMA/K-Means;

3. Custo 40% inferior a soluções similares (estimados de R\$ 3.227,40/UBS vs média estimada de R\$ 5.200/UBS do mercado) \[24\];

**Poder de Barganha dos Fornecedores (Intensidade: Baixa)**

O poder de barganha dos fornecedores é relativamente baixo devido à:

* Disponibilidade de componentes IoT padronizados (sensores, microcontroladores) de múltiplos fornecedores globais;

* Padronização de protocolos de comunicação permite flexibilidade na escolha de hardwares;

* Fornecedores de infraestrutura de nuvem (AWS, Google Cloud, Azure) operam em mercado competitivo;

Esta força favorável permite gerenciamento eficiente de custos e substituição de fornecedores sem impacto significativo na solução. Essa força em específico pode ser mais afetada por mudanças regulatórias e de taxação de produtos/serviços importados do que dos fornecedores em si.

**Poder de Barganha dos Compradores (Intensidade: Alta)**

O poder de barganha dos compradores (prefeituras municipais, gestores de saúde) é significativo devido a:

* Processo de licitação pública (Lei 8.666/93) \[25\] que prioriza o menor preço;

* Sensibilidade orçamentária no setor público de saúde;

* Exigência de conformidade com normas técnicas específicas (ANVISA, RNDS);

Para mitigar esta força, nossa estratégia inclui:

* Demonstração de ROI claro e relativamente rápido (10 meses);

* Conformidade comprovada com normas regulatórias;

* Diferenciação pela integração única de funcionalidades(monitoramento energético e de estoque, controle de temperatura);

**Ameaça de Novos Entrantes (Intensidade: Moderada)**

Barreiras significativas protegem parcialmente o mercado:

* Requisitos ANVISA RDC 430/2020 para certificação de sistemas médicos \[13\];

* Necessidade de integração com RNDS via FHIR Release 4 \[20\];

* Curva de aprendizado em algoritmos de otimização energética LSTM-ARIMA;

* Processos de licitação com diversas regras de participação, como tamanho do capital da empresa, tempo de CNPJ, pré-requisitos de contribuição em processos anteriores;

Entretanto, a padronização crescente de tecnologias IoT e a disponibilidade de plataformas de desenvolvimento web facilitam a entrada de competidores que possuam os recursos e aporte adequados.

**Ameaça de Produtos Substitutos (Intensidade: Baixa)**

A ameaça de produtos substitutos é baixa considerando que:

* Soluções manuais (status quo atual) são reconhecidamente inadequadas;

* O custo de falha é elevado (R\$ 1,2 bilhão/ano em perdas de vacinas) \[1\];

* A ineficiência energética atual não é sustentável;

Substitutos potenciais incluem sistemas básicos de alarmes ou soluções parciais de monitoramento, mas nenhum oferece a integração e otimização da solução proposta.

**4.2 Vantagem Competitiva**

A vantagem competitiva da solução fundamenta-se em diferenciação através de integração única de funcionalidades, especialização no mercado brasileiro de UBS e foco em sustentabilidade energética e de insumos imunobiológicos.

**Diferenciação por Integração**

A principal vantagem competitiva reside na integração inédita de múltiplas funcionalidades em uma plataforma única:

* Monitoramento de temperatura para preservação de vacinas;

* Gestão energética inteligente com algoritmos preditivos;

* Controle automatizado de inventário de imunobiológicos;

* Interface unificada para gestão municipal em tempo real;

Esta abordagem holística endereça simultaneamente múltiplos desafios críticos enfrentados pelas UBS, oferecendo valor superior à soma de soluções individuais.

**Especialização no Contexto Brasileiro**

A solução foi especificamente projetada para o contexto do SUS e das UBS brasileiras, considerando:

* Conformidade com regulamentações nacionais (ANVISA, RNDS);

* Adaptação às limitações de infraestrutura tecnológica dos municípios;

* Compreensão dos processos operacionais específicos das UBS;

* Integração com sistemas legados municipais;

Este conhecimento contextual cria barreiras de entrada para competidores internacionais e diferenciação em relação a soluções genéricas.

**Foco em Sustentabilidade**

O foco em sustentabilidade energética alinha-se com tendências crescentes de responsabilidade ambiental no setor público e oportunidades de financiamento através de programas de eficiência energética. A capacidade de demonstrar:

* Redução mensurável no consumo energético;

* Diminuição na emissão de gases de efeito estufa;

* Contribuição para objetivos de desenvolvimento sustentável;

* ROI claro e rápido (10 meses);

Este posicionamento fortalece a proposta de valor e facilita a aprovação de projetos em um contexto de orçamentos públicos limitados.

**Criação de Valor**

A estratégia de criação de valor para clientes baseia-se em múltiplos benefícios tangíveis:

* Economia financeira direta: estimados R\$44.640,49/ano (aprox. 1.2x do custo de implementação) para as 11 UBS de São Carlos;

* Conformidade regulatória automatizada;

* Redução considerável de perdas de vacinas por infraestrutura e controle de estoque precários;

* Liberação de tempo de profissionais de saúde para atividades de maior valor;

**Alianças Estratégicas**

Parcerias estratégicas potencializam nossa vantagem competitiva:

* Colaboração com a USP-São Carlos para validação acadêmica e pesquisa aplicada;

* Alianças com associações de municípios para escala regional;

* Parcerias com programas de eficiência energética da ANEEL/CPFL para financiamento;

Estas alianças ampliam nossa capacidade de implementação, reduzem barreiras de entrada em futuros municípios e fortalecem a credibilidade da solução.

A combinação destas vantagens posiciona nossa solução como referência no mercado de sistemas inteligentes para UBS, com potencial de expansão para outras unidades de saúde e municípios brasileiros.

**5\. REFERÊNCIAS BIBLIOGRÁFICAS**

\[1\] TRIBUNAL DE CONTAS DA UNIÃO. Auditoria sobre perdas de vacinas no Brasil. Brasília: TCU, 2023\.

\[2\] AGÊNCIA BRASIL. TCU aponta perdas de R\$1,2 bilhão com vacinas vencidas. 2023\. Disponível em: [https\://agenciabrasil.ebc.com.br/saude/noticia/2023-10/tcu-aponta-perdas-de-r-12-bilhao-com-vacinas-vencidas](https://agenciabrasil.ebc.com.br/saude/noticia/2023-10/tcu-aponta-perdas-de-r-12-bilhao-com-vacinas-vencidas)

\[3\] ANVISA. Resolução RDC nº 430/2020. Regulamenta as boas práticas de distribuição, armazenamento e transporte de medicamentos. Brasília: ANVISA, 2020\.

\[4\] PREFEITURA DE SÃO CARLOS. Unidades de Saúde. 2024\. Disponível em: [http\://www\.saocarlos.sp.gov.br/index.php/saude/115420-unidades-de-saude.html](http://www.saocarlos.sp.gov.br/index.php/saude/115420-unidades-de-saude.html)

\[5\] G1 SÃO CARLOS. Sistema criado na UFSCar monitora temperatura de local onde ficam vacinas em São Carlos. 2021\. Disponível em: [https\://g1.globo.com/sp/sao-carlos-regiao/noticia/2021/01/28/sistema-criado-na-ufscar-monitora-temperatura-de-local-onde-ficam-vacinas-em-sao-carlos.ghtml](https://g1.globo.com/sp/sao-carlos-regiao/noticia/2021/01/28/sistema-criado-na-ufscar-monitora-temperatura-de-local-onde-ficam-vacinas-em-sao-carlos.ghtml)

\[6\] OLIVEIRA, V.C. et al. Conservação de vacinas em unidades básicas de saúde: análise diagnóstica em municípios mineiros. Revista Brasileira de Enfermagem, v. 72, n. 4, p. 1111-1118, 2019\. Disponível em: [https\://www\.scielo.br/j/reben/a/4JjkNN4G5wF4Tcn3fsrwVCG/?lang=pt](https://www.scielo.br/j/reben/a/4JjkNN4G5wF4Tcn3fsrwVCG/?lang=pt)

\[7\] CONSELHO BRASILEIRO DE CONSTRUÇÃO SUSTENTÁVEL. Consumo energético de UBS em Sorocaba-SP. 2018\. Disponível em: [https\://cidadeseficientes.cbcs.org.br/wp-content/uploads/pdf/Analise-dados-edificios\_SCB.pdf](https://cidadeseficientes.cbcs.org.br/wp-content/uploads/pdf/Analise-dados-edificios_SCB.pdf)

\[8\] ANEEL. Projeto de eficiência energética em hospitais para enfrentamento da COVID-19 é concluído. 2022\. Disponível em: [https\://www\.gov.br/aneel/pt-br/assuntos/noticias/2022/projeto-de-eficiencia-energetica-em-hospitais-para-enfrentamento-da-covid-19-e-concluido](https://www.gov.br/aneel/pt-br/assuntos/noticias/2022/projeto-de-eficiencia-energetica-em-hospitais-para-enfrentamento-da-covid-19-e-concluido)

\[9\] SENSORWEB. Guia de Boas Práticas na Conservação de Vacinas. 2019\. Disponível em: [https\://sensorweb.com.br/wp-content/uploads/2019/03/Guia-Boas-Práticas-Conservação-Vacinas.pdf](https://sensorweb.com.br/wp-content/uploads/2019/03/Guia-Boas-Pr%C3%A1ticas-Conserva%C3%A7%C3%A3o-Vacinas.pdf)

\[10\] PREFEITURA DE LAGES. Saúde implementa sistema para monitoramento de temperatura em câmaras de vacinas. 2023\. Disponível em: [https\://www\.saudelages.sc.gov.br/noticia/view?id=1399](https://www.saudelages.sc.gov.br/noticia/view?id=1399)

\[11\] PORTAL NEWS. EDP conclui projeto de eficiência energética no Pronto Atendimento em Poá. 2025\. Disponível em: [https\://portalnews.com.br/cidades/2025/02/edp-conclui-projeto-de-eficiencia-energetica-no-pronto-atendimento-em-poa](https://portalnews.com.br/cidades/2025/02/edp-conclui-projeto-de-eficiencia-energetica-no-pronto-atendimento-em-poa)

\[12\] GOVERNO DA PARAÍBA. Hospital Regional de Patos é contemplado com projeto de eficiência energética da Energisa. 2022\. Disponível em: [https\://paraiba.pb.gov.br/noticias/hospital-regional-de-patos-e-contemplado-com-projeto-de-eficiencia-energetica-da-energisa](https://paraiba.pb.gov.br/noticias/hospital-regional-de-patos-e-contemplado-com-projeto-de-eficiencia-energetica-da-energisa)

\[13\] ANVISA. RELATÓRIO DE MÉTRICAS DE INSPEÇÕES DE BPC 2023 COORDENAÇÃO DE PESQUISA CLÍNICA EM MEDICAMENTOS E PRODUTOS BIOLÓGICOS – COP. 2023\. Disponível em: [https\://www\.gov.br/anvisa/pt-br/assuntos/medicamentos/pesquisaclinica/publicacoes-1/relatorios-anuais/copec-\_metricas-de-inspecao-de-bpc\_2023.pdf](https://www.gov.br/anvisa/pt-br/assuntos/medicamentos/pesquisaclinica/publicacoes-1/relatorios-anuais/copec-_metricas-de-inspecao-de-bpc_2023.pdf)

\[14\] IEEE INTERNET OF THINGS JOURNAL. MQTT Protocol Analysis for Critical IoT Applications. 2024\.

\[15\] IEEE. Performance Evaluation of Asynchronous JavaScript Technology for IoT Systems. 2023\.

\[16\] JOURNAL OF DATABASE MANAGEMENT. PostgreSQL for IoT Applications: Performance and Optimization Strategies. 2024\. Disponível em: [https\://www\.researchgate.net/publication/330285201\_Database\_Systems\_Performance\_Evaluation\_for\_IoT\_Applications](https://www.researchgate.net/publication/330285201_Database_Systems_Performance_Evaluation_for_IoT_Applications)

\[17\] INFLUXDATA. Time Series Database Benchmarks for IoT Applications. 2023\. Disponível em: [https\://www\.researchgate.net/publication/363128579\_Performance\_Study\_of\_Time\_Series\_Databases](https://www.researchgate.net/publication/363128579_Performance_Study_of_Time_Series_Databases)

\[18\] ACM COMPUTING SURVEYS. Modern Web Frameworks for IoT Dashboard Development. 2023\.

\[19\] JOURNAL OF NETWORK AND COMPUTER APPLICATIONS. Cloud Infrastructure Requirements for Critical IoT Systems. 2024\.

\[20\] MINISTÉRIO DA SAÚDE. Rede Nacional de Dados em Saúde (RNDS). 2023\. Disponível em: [https\://www\.gov.br/saude/pt-br/composicao/seidigi/rnds](https://www.gov.br/saude/pt-br/composicao/seidigi/rnds)

\[21\] IEEE TRANSACTIONS ON NEURAL NETWORKS AND LEARNING SYSTEMS. Hybrid LSTM-ARIMA Models for Time Series Prediction in IoT Systems. 2023\.

\[22\] APPLIED ENERGY. Machine Learning Models for Energy Consumption Forecasting in Healthcare Facilities. 2024\.

\[23\] JOURNAL OF HEALTHCARE ENGINEERING. Clustering Techniques for Personalized Healthcare Facility Management. 2023\.

\[24\] 1NCE. Principais considerações ao planejar um projeto de IoT. Disponível em: [https\://www\.1nce.com/pt-br/recursos/news/blog/iot-no-planejamento-de-projetos](https://www.1nce.com/pt-br/recursos/news/blog/iot-no-planejamento-de-projetos)

\[25\] PLANALTO GOV BRASIL. LEI Nº 8.666, DE 21 DE JUNHO DE 1993\. Disponível em: [https\://www\.planalto.gov.br/ccivil\_03/leis/l8666cons.htm](https://www.planalto.gov.br/ccivil_03/leis/l8666cons.htm)

\[26\] IME\_USP. Linguagem C++.  Silvio do Lago Pereira, Disponível em https\://www\.ime.usp.br/\~slago/slago-C++.pdf

\[27\] SQLite-When to Use. Disponível em https\://sqlite.org/whentouse.html 

**6\. DISCRIMINAÇÃO DO USO DE IA NO TRABALHO**

Utilização de IA ocorreu nas seguintes frentes:

1. Geração de sugestões de infográficos, incluindo logo da empresa fictícia. Os infos foram editados extensivamente, com aproveitamento da paleta de cores e dos ícones sugeridos;(Mateus Saracuza)  
2. Revisão do texto final(Marcos Reballo) e checagem de referências, com posterior checagem humana(Pedro Kemp);  
3. Geração de sugestões de telas do SI, que foram utilizadas de base para produção humana completa via Figma;(Arthur Azorli/Nícolas Scorza);  
4. Cálculo do ROI, baseando-se na lista de equipamentos sugeridos pelo nosso especialista de embarcados (Arthur Azorli);  
5. Geração do texto “Resumo Executivo” sobre panorama geral da proposta;

**7\. LINK DO PROTÓTIPO**

Versão Mobile: [https\://www\.figma.com/proto/Ngcu92GsupdBB0KtYSKLar/Vacinas-Mobile](https://www.figma.com/proto/Ngcu92GsupdBB0KtYSKLar/Vacinas-Mobile)

Versão Compatível com visualização em PC: [https\://pedrokemp.github.io/Vacinas/](https://pedrokemp.github.io/Vacinas/)

*Addendo:* Foram criadas telas somente para versão mobile, a segunda versão acima é para melhor visualização em telas de notebooks e afins. Não criamos versão responsiva do protótipo.

[^1]:  *Valor muito baixo para menção separada de custos de hardware (R\$12,00)*
