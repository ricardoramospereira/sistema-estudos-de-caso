PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE estudos (
                        id INTEGER PRIMARY KEY,
                        titulo TEXT
                      );
INSERT INTO estudos VALUES(1,'AWS - Criando Conta');
INSERT INTO estudos VALUES(2,'AWS - MFA para usuário "root"');
INSERT INTO estudos VALUES(3,'Respostas de segurança e informações de contato');
INSERT INTO estudos VALUES(4,'AWS - CLI');
INSERT INTO estudos VALUES(5,'AWS - IAM');
INSERT INTO estudos VALUES(6,'AWS - Modelos de aquisição');
CREATE TABLE passos (
                        id INTEGER PRIMARY KEY,
                        estudo_id INTEGER,
                        passo TEXT,
                        problema TEXT,
                        resolvido INTEGER,
                        FOREIGN KEY (estudo_id) REFERENCES estudos(id)
                      );
INSERT INTO passos VALUES(2,'mais um teste','Configurando','sem problemas',0);
INSERT INTO passos VALUES(3,1,'Documentação: https://docs.aws.amazon.com/pt_br/','',0);
INSERT INTO passos VALUES(4,1,replace('Freet tier - Nível Gratuíto.\nhttps://aws.amazon.com/pt/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all','\n',char(10)),'',0);
INSERT INTO passos VALUES(5,1,'Criação da Conta: Seguir todos as etapas.','O usuário ROOT só é pra ser usado para criação, mas não para uso diário',0);
INSERT INTO passos VALUES(6,2,'Documentação: https://aws.amazon.com/pt/iam/features/mfa/?nc1=h_ls','',0);
INSERT INTO passos VALUES(7,2,'Seguir os passos da atualização','Tirar print do QRCode para um possível problema futuro',0);
INSERT INTO passos VALUES(8,3,replace('Configurações Recomendadas: \n* image user \n* Account\n* Alternate Contacts\n        Preencher todos os campos\n* Configure Security Challenge Questions\n        Configurar as 3 questões de segurança         (recuperar conta)\n\nOBS: Umas das questões selecionar "Security Chanllenge Response e nessa opção basta gerar uma senha com 100 caracteres e guardar em um lugar seguro','\n',char(10)),'',0);
INSERT INTO passos VALUES(9,4,'Documentação: https://docs.aws.amazon.com/pt_br/cli/latest/userguide/cli-chap-welcome.html','',0);
INSERT INTO passos VALUES(10,5,replace('Criando usuário no IAM:\n\n* IAM\n* User group\n* Name de group (administrators)\n* Attachpermissions policies (AdministratorAccess)\n* Create user \n* Marcar a opção de Provide user access to the AWS Management Console (para uso CLI)\n* Add user to group\n\n','\n',char(10)),'Obs: O ideal é criar sua própria politica (conceito minimo privilégio), e não usar as políticas gerenciadas da AWS ',0);
INSERT INTO passos VALUES(11,6,'Na Console - Procurar serviços "EC2"','',0);
INSERT INTO passos VALUES(12,6,replace('Na lista a esquerda irá ter as opções:\n 	- Savings Plans\n	- Reserved Instances\n	- Spot requests','\n',char(10)),'Não há a opção de "sob demanda" porque já é por padrão.',0);
INSERT INTO passos VALUES(13,6,replace('Reserved Instances:\n - Clicar em Purchase Reserved Instances\n - Platform (escolher a plataforma)\n - Tenancy (default)\n - Offering class:\n	- Standard (se for essa opção padrão não da pra converter depois)\n	- Convertible (Pode-se ser convertido posterior)\n - Instance type (definir)\n - Term (O tempo)\n - Payment option\n - Seach (clicar)\n','\n',char(10)),'Se o offering class for a padrão não há como alterar a Instance type uma vez escolhido',0);
INSERT INTO passos VALUES(14,6,replace('Savings Plans:\n\n- Clicar em um link\n- Purchase a Savings Plan\n- Purchase details - Savings Plans type\n	- Compute savings Plans\n	- EC2 Instance Saving Plans \n	- SagMaker Saving Plans\n\n- Term (1 ou 3 anos)\n- Region \n- Instance family (t2, por exemplo)\n- hourly commitment (qual o valor hora que vamos aplicar no saving plans)\n- Payment option\n- Start data (defina o dia e horário do contrato)\n\n','\n',char(10)),replace('- Selecionar EC2 Instance Saving Plans\n\nObs: Se tiver uma máquina rodando clique em "Recommendations" que vai ter recomendação mais em conta baseada nos gastos que estamos tendo com a ativa','\n',char(10)),0);
INSERT INTO passos VALUES(15,6,replace('Spot Requests:\n\n - Request Spot Instances\n ','\n',char(10)),'',0);
COMMIT;
