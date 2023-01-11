import mysql.connector
import sys

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "Bambam&xx12",
    "database": "pathfinder"
}

connection = mysql.connector.connect(**db_config)

friend_requirements = {
    "requirements": [
        {
            "content": "Ter, no mínimo, dez anos de idade.",
            "requirementGroupId": 1,
            "classId": 1
        },
        {
            "content": "Ser membro ativo do Clube de Desbravadores.",
            "requirementGroupId": 1,
            "classId": 1
        },
        {
            "content": "Memorizar e explicar o Voto e a Lei do Desbravador.",
            "requirementGroupId": 1,
            "classId": 1
        },
        {
            "content": "Ler o livro do Clube de Leitura do ano em curso.",
            "requirementGroupId": 1,
            "classId": 1
        },
        {
            "content": "Ler o livro Vaso de Barro.",
            "requirementGroupId": 1,
            "classId": 1
        },
        {
            "content": "Participar ativamente da classe bíblica do seu Clube.",
            "requirementGroupId": 1,
            "classId": 1
        },
        {
            "content": "Memorizar e demonstrar o seu conhecimento:",
            "requirementGroupId": 2,
            "classId": 1,
            "subRequirements": [
                {
                    "content": "Criação: O que Deus criou em cada dia da Criação.",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "10 Pragas: Quais as pragas que caíram sobre o Egito.",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "12 Tribos: O nome de cada uma das 12 tribos de Israel.",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "39 livros do Antigo Testamento e desmonstrar habilidade para encontrar qualquer um deles.",
                    "subRequirementTypeId": 1
                }
            ]
        },
        {
            "content": "Ler e explicar os versos abaixo:",
            "requirementGroupId": 2,
            "classId": 1,
            "subRequirements": [
                {
                    "content": "João 3:16",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "Efésios 6:1-3",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "2 Timóteo 3:16",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "Salmo 1",
                    "subRequirementTypeId": 2
                }
            ]
        },
        {
            "content": "Leitura bíblica:",
            "requirementGroupId": 2,
            "classId": 1,
            "subRequirements": [
                {
                    "content": "Gn 1, 2, 3, 4:1-16, 6:11-22, 7, 8, 9:1-19, 11:1-9, 12:1-10, 13, 14;18-24, 15, 17:1-8;15-22, 18:1-15, 18:16-33, 19:1-29, 21:1-21, 22:1-19, 23, 24:1-46,48, 24:52-67, 27, 28, 29, 30:25-31; 31:2-3, 17-18, 32, 33, 37, 39, 40, 41, 42, 43, 44, 45, 47, 50",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "Êx 1, 2, 3, 4:1-17; 27-31, 5, 7, 8, 9, 10, 11, 12, 13:17-22; 14, 15:22-27; 16, 17, 18, 19, 20, 24, 32, 33, 34:1-14; 29-35, 35:4-29 e 40.",
                    "subRequirementTypeId": 2
                }
            ]
        },
        {
            "content": "Dedicar duas horas ajudando alguém em sua comunidade, através de duas das seguintes atividades:",
            "requirementGroupId": 3,
            "classId": 1,
            "subRequirements": [
                {
                    "content": "Visitar alguém que precisa de amizade e orar com essa pessoa.",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Oferecer alimento a alguém carente.",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Participar de um projeto ecológico ou educativo.",
                    "subRequirementTypeId": 1
                }
            ]
        },
        {
            "content": "Escrever uma redação explicando como ser um bom cidadão no lar e na escola.",
            "requirementGroupId": 3,
            "classId": 1
        },
        {
            "content": "Mencionar dez qualidades de um bom amigo e apresentar quatro situações diárias onde você praticou a Regra Áurea de Mateus 7:12.",
            "requirementGroupId": 4,
            "classId": 1
        },
        {
            "content": "Saber cantar o hino nacional de seu país e conhecer sua história. Saber o nome do autor da letra e da música do hino.",
            "requirementGroupId": 4,
            "classId": 1
        },
        {
            "content": "Completar uma das seguintes especialidades:",
            "requirementGroupId": 5,
            "classId": 1,
            "subRequirements": [
                {
                    "content": "Natação Principiante 1",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Cultura física",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Nós e amarras",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Segurança básica na água",
                    "subRequirementTypeId": 1
                }
            ]
        },
        {
            "content": "Utilizando a experiência de Daniel:",
            "requirementGroupId": 5,
            "classId": 1,
            "subRequirements": [
                {
                    "content": "Explicar os princípios de temperança que ele defendeu ou participar em uma apresentação ou encenação sobre Daniel 1.",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Memorizar e explicar Daniel 1:8.",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Escrever seu compromisso pessoal de seguir um estilo de vida saudável.",
                    "subRequirementTypeId": 1
                }
            ]
        },
        {
            "content": "Aprender os princípios de uma dieta saudável e ajudar a preparar um quadro com os grupos básicos de alimentos.",
            "requirementGroupId": 5,
            "classId": 1
        },
        {
            "content": "Através da observação, acompanhar todo o processo de planejamento até a execução de uma caminhada de 5 quilômetros.",
            "requirementGroupId": 6,
            "classId": 1
        },
        {
            "content": "Completar uma das seguintes especialidades:",
            "requirementGroupId": 7,
            "classId": 1,
            "subRequirements": [
                {
                    "content": "Felinos",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Cães",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Mamíferos",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Sementes",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Aves de estimação",
                    "subRequirementTypeId": 1
                }
            ]
        },
        {
            "content": "Aprender e demonstrar uma maneira para purificar a água e escreve rum parágrafo destacando o significado de Jesus como a água da vida.",
            "requirementGroupId": 7,
            "classId": 1
        },
        {
            "content": "Aprender e motar três diferentes tipos de barracas em locais apropriados.",
            "requirementGroupId": 7,
            "classId": 1
        },
        {
            "content": "Demonstrar como cuidar corretamente de uma corda. Fazer e explicar o uso prático dos seguintes nós:",
            "requirementGroupId": 8,
            "classId": 1,
            "subRequirements": [
                {
                    "content": "Simples",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Cego",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Direito",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Cirurgião",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Lais de guia",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Lais de guia duplo",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Escota",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Catau",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Pescador",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Fateixa",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Volta do fiel",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Nó de gancho",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Volta da ribeira",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Ordinário",
                    "subRequirementTypeId": 1
                },
            ]
        },
        {
            "content": "Completar a especialidade de Acampamento 1",
            "requirementGroupId": 8,
            "classId": 1
        },
        {
            "content": "Apresentar 10 regras para uma caminhada e explicar o que fazer quando estiver perdido.",
            "requirementGroupId": 8,
            "classId": 1
        },
        {
            "content": "Aprender os sinais para seguir uma pista. Preparar e seguir uma pista de no mínimo, 10 sinais, que também possa ser seguida por outros.",
            "requirementGroupId": 8,
            "classId": 1
        },
        {
            "content": "Completar uma especialidade na área de Artes e habilidades manuais.",
            "requirementGroupId": 9,
            "classId": 1
        },
        {
            "content": "Memorizar, cantar ou tocar o Hino dos Desbravadores e conhecer a história do hino.",
            "requirementGroupId": 10,
            "classId": 1
        },
        {
            "content": "Em consulta com seu líder, escolher um dos seguintes personagens do Antigo Testamento e conversar com seu grupo sobre o amor e cuidado de Deus e o livramento demonstrado na vida do personagem escolhido.",
            "requirementGroupId": 10,
            "classId": 1,
            "subRequirements": [
                {
                    "content": "José",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Jonas",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Ester",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Rute",
                    "subRequirementTypeId": 1
                }
            ]
        },
        {
            "content": "Levar pelo menos dois amigos não adventistas á Escola Sabatina ou ao Clube de Desbravadores.",
            "requirementGroupId": 10,
            "classId": 1
        },
        {
            "content": "Conhecer os princípios de higiene, de boas maneiras à mesa, e como se comportar diante de pessoas que tenham diferentes idades. Demonstrar e explicar como estas boas maneiras podem ser úteis nas reuniões e acampamentos do clube.",
            "requirementGroupId": 10,
            "classId": 1
        },
        {
            "content": "Fazer a especialidade de Arte de acampar.",
            "requirementGroupId": 10,
            "classId": 1
        },
        {
            "content": "Conhecer e identificar 10 flores silvestres e 10 insetos de sua região.",
            "requirementGroupId": 10,
            "classId": 1
        },
        {
            "content": "Começar uma fogueira com apenas um fósforo, usando materiais naturais, e matê-la acesa.",
            "requirementGroupId": 10,
            "classId": 1
        },
        {
            "content": "Usar corretament uma faca, facão ou machadinha e conhecer dez regras para usá-los com segurança.",
            "requirementGroupId": 10,
            "classId": 1
        },
        {
            "content": "Escolher e completar uma especialidade em uma das áreas abaixo:",
            "requirementGroupId": 10,
            "classId": 1,
            "subRequirements": [
                {
                    "content": "Atividades missionárias e comunitárias.",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Atividades agrícolas e afins.",
                    "subRequirementTypeId": 1
                }
            ]
        }
    ]
}

companion_requirements = {
    "requirements": [
        {
            "content": "Ter, no mínimo, 11 anos de idade.",
            "requirementGroupId": 1,
            "classId": 2
        },
        {
            "content": "Ser membro ativo do Clube de Desbravadores.",
            "requirementGroupId": 1,
            "classId": 2
        },
        {
            "content": "Ilustrar de forma criativa o significado do Voto do Desbravador.",
            "requirementGroupId": 1,
            "classId": 2
        },
        {
            "content": "Ler o livro do Clube de Leitura do ano em curso e escrever um parágrafo sobre o que mais lhe chamou atenção ou considerou importante.",
            "requirementGroupId": 1,
            "classId": 2
        },
        {
            "content": "Ler o livro Caminho a Cristo.",
            "requirementGroupId": 1,
            "classId": 2
        },
        {
            "content": "Participar ativamente da classe bíblica do seu clube.",
            "requirementGroupId": 1,
            "classId": 2
        },
        {
            "content": "Memorizar e demonstrar o seu conhecimento:",
            "requirementGroupId": 2,
            "classId": 2,
            "subRequirements": [
                {
                    "content": "10 Mandamentos: A Lei de Deus dada a Moisés.",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "27 livros do Novo Testamento e demonstrar habilidade para encontrar qualquer um deles.",
                    "subRequirementTypeId": 1
                }
            ]
        },
        {
            "content": "Memorizar e recitar os versos abaixo:",
            "requirementGroupId": 2,
            "classId": 2,
            "subRequirements": [
                {
                    "content": "Isa. 41:9-10",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "Heb. 13:5",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "Prov. 22:6",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "1 João 1:9",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "Salmo 8",
                    "subRequirementTypeId": 2
                }
            ]
        },
        {
            "content": "Leitura bíblica:",
            "requirementGroupId": 2,
            "classId": 2,
            "subRequirements": [
                {
                    "content": "Lv 11",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "Nm 9:15-23, 11, 12, 13, 14:1-38, 16, 17, 20:1-13; 22-29, 21:4-9, 22, 23; 24:1-10",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "Dt 1:1-17; 4:1-8, 32:1-43, 33, 34",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "Js 1, 2, 3, 4, 5:10; 6, 7, 9, 24:1-15; 29",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "Jz 6, 7, 13:1-18; 14, 15, 16",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "Rt 1, 2, 3, 4",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "1 Sm 1, 2, 3, 4, 5, 6, 8, 9, 10, 11:12-15, 12, 13, 15, 16, 17, 18:1-19, 20, 21:1-7; 22, 24, 25, 26, 31",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "2 Sm 1, 5, 6, 7, 9, 11; 12:1-25, 15, 18",
                    "subRequirementTypeId": 2
                }
            ]
        },
        {
            "content": "Em consulta com o seu conselheiro, escolher um dos seguintes temas:",
            "requirementGroupId": 2,
            "classId": 2,
            "subRequirements": [
                {
                    "content": "Uma parábola de Jesus",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Um milagre de Jesus",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "O Sermão da Montanha",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Um sermão sobre a segunda vinda de Cristo",
                    "subRequirementTypeId": 1
                }
            ]
        },
        {
            "content": "Escolher um item abaixo para demonstrar seu conhecimento sobre o tema escolhido:",
            "requirementGroupId": 2,
            "classId": 2,
            "subRequirements": [
                {
                    "content": "Troca de ideias com o seu conselheiro",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Atividade que integre todo o grupo",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Redação",
                    "subRequirementTypeId": 1
                }
            ]
        },
        {
            "content": "Planejar e dedicar pelo menos duas horas servindo sua comunidade e demonstrando companheirismo a alguém, de maneira prática.",
            "requirementGroupId": 3,
            "classId": 2
        },
        {
            "content": "Participar de um projeto que beneficiará sua comunidade ou igreja.",
            "requirementGroupId": 3,
            "classId": 2
        },
        {
            "content": "Conversar com seu conselheiro ou unidade sobre como respeitar pessoas de diferentes culturas, raças e sexo.",
            "requirementGroupId": 4,
            "classId": 2
        },
        {
            "content": "Memorizar e explicar 1 Coríntios 9:24-27.",
            "requirementGroupId": 5,
            "classId": 2
        },
        {
            "content": "Conversar com seu líder sobre a aptidão física e os exercícios físicos regulares que se relacionam com uma vida saudável.",
            "requirementGroupId": 5,
            "classId": 2
        },
        {
            "content": "Aprender sobre os prejuízos que o cigarro causa à saúde e escrever seu compromisso de não fazer uso do fumo.",
            "requirementGroupId": 5,
            "classId": 2
        },
        {
            "content": "Completar uma das seguintes especialidades:",
            "requirementGroupId": 5,
            "classId": 2,
            "subRequirements": [
                {
                    "content": "Natação principiante 2",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Acampamento 2",
                    "subRequirementTypeId": 1
                }
            ]
        },
        {
            "content": "Dirigir ou colaborar em uma meditação criativa para sua unidade ou Clube.",
            "requirementGroupId": 6,
            "classId": 2
        },
        {
            "content": "Ajudar no planejamento de excursão ou acampamento com sua unidade ou clube, envolvendo pelo menos um pernoite.",
            "requirementGroupId": 6,
            "classId": 2
        },
        {
            "content": "Completar duas das seguintes especialidades:",
            "requirementGroupId": 7,
            "classId": 2,
            "subRequirements": [
                {
                    "content": "Anfíbios",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Aves",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Aves domésticas",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Pecuária",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Reptéis",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Moluscos",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Árvores",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Arbustos",
                    "subRequirementTypeId": 1
                }
            ]
        },
        {
            "content": "Recapitular o estudo da Criação e fazer um diário por sete dias registrando suas observações do que foi criado em cada dia correspondente.",
            "requirementGroupId": 7,
            "classId": 2
        },
        {
            "content": "Descobrir os pontos cardeais sem a ajuda de uma bússola e desenhar a Rosa dos Ventos.",
            "requirementGroupId": 8,
            "classId": 2
        },
        {
            "content": "Participar de um acampamento de final de semana e fazer um relatório destacando o que mais lhe impressionou positivamente.",
            "requirementGroupId": 8,
            "classId": 2
        },
        {
            "content": "Aprender ou recapitular os seguintes nós:",
            "requirementGroupId": 8,
            "classId": 2,
            "subRequirements": [
                {
                    "content": "Oito",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Volta do salteador",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Duplo",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Caminhoneiro",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Direito",
                    "subRequirementTypeId": 1,
                },
                {
                    "content": "Volta do Fiel",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Escota",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Lais de Guia",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Simples",
                    "subRequirementTypeId": 1
                }
            ]
        },
        {
            "content": "Completar uma especialidade não realizada anteriorment na seção de Artes e habilidades manuais.",
            "requirementGroupId": 9,
            "classId": 2
        },
        {
            "content": "Aprender e demonstrar a composição, significado e uso correto da Bandeira Nacional.",
            "requirementGroupId": 10,
            "classId": 2
        },
        {
            "content": "Ler a primeira visão de Ellen White e discutir como Deus usa os profetas para apresentar Sua mensagem à igreja (ver Primeiros Escritos, p. 13 a 20).",
            "requirementGroupId": 10,
            "classId": 2
        },
        {
            "content": "Participar de uma atividade missionária ou comunitária, envolvendo também um amigo.",
            "requirementGroupId": 10,
            "classId": 2
        },
        {
            "content": "Conversar com seu conselheiro ou unidade sobre como demonstrar respeito pelos seus pais ou responsáveis e fazer uma lista mostrando como cuidam de você.",
            "requirementGroupId": 10,
            "classId": 2
        },
        {
            "content": "Participar de uma caminhada de 6 quilômetros, preparand, ao final, um relatório de uma página.",
            "requirementGroupId": 10,
            "classId": 2
        },
        {
            "content": "Escolher um dos seguintes itens:",
            "requirementGroupId": 10,
            "classId": 2,
            "subRequirements": [
                {
                    "content": "Assistir a um Curso como deixar de fumar",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Assistir a dois filmes sobre saúde",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Elaborar um cartaz sobre o prejuízo das drogas",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Ajudar a preparar material para uma exposição ou passeata sobre saúde",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Pesquisar na internet informações sobre saúde e escrever uma página sobre os resultados encontrados",
                    "subRequirementTypeId": 1
                }
            ]
        },
        {
            "content": "Identificar e descrever 12 aves nativas e 12 árvores nativas.",
            "requirementGroupId": 10,
            "classId": 2
        },
        {
            "content": "Participar de uma das seguintes cerimônias e sugerir ideias criativas e como realizá-las.",
            "requirementGroupId": 10,
            "classId": 2,
            "subRequirements": [
                {
                    "content": "Investidura",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Admissão em lenço",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Dia Mundial do Desbravador",
                    "subRequirementTypeId": 1
                }
            ]
        },
        {
            "content": "Preparar uma refeição em uma fogueira durante um acampamento do clube ou unidade.",
            "requirementGroupId": 10,
            "classId": 2
        },
        {
            "content": "Preparar um quadro com 15 nós diferentes.",
            "requirementGroupId": 10,
            "classId": 2
        },
        {
            "content": "Completar a especialidade de Excursionismo pedestre com mochila.",
            "requirementGroupId": 10,
            "classId": 2
        },
        {
            "content": "Completar uma especialidade não realizada anteriormente.",
            "requirementGroupId": 10,
            "classId": 2,
            "subRequirements": [
                {
                    "content": "Habilidades domésticas",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Ciência e saúde",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Atividades missionárias e comunitárias",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Atividades agrícolas e afins",
                    "subRequirementTypeId": 1
                }
            ]
        }
    ]
}

researcher_requirements = {
    "requirements": [
        {
            "content": "Ter, no mínimo, 12 anos de idade.",
            "requirementGroupId": 1,
            "classId": 3
        },
        {
            "content": "Ser membro ativo do Clube de Desbravadores.",
            "requirementGroupId": 1,
            "classId": 3
        },
        {
            "content": "Demonstrar sua compreensão do significado da Lei do Desbravador através de uma das seguintes atividades.",
            "requirementGroupId": 1,
            "classId": 3,
            "subRequirements": [
                {
                    "content": "Representação",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Debate",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Redação",
                    "subRequirementTypeId": 1
                }
            ]
        },
        {
            "content": "Ler o livro do Clube de Leitura do ano em curso e escrever dois parágrafos sobre o que mais lhe chamou atenção ou considerou importante.",
            "requirementGroupId": 1,
            "classId": 3
        },
        {
            "content": "Ler o livro Além da Magia.",
            "requirementGroupId": 1,
            "classId": 3
        },
        {
            "content": "Participar ativamente da classe bíblica do seu clube.",
            "requirementGroupId": 1,
            "classId": 3
        },
        {
            "content": "Memorizar e demonstrar o seu conhecimento:",
            "requirementGroupId": 2,
            "classId": 3,
            "subRequirements": [
                {
                    "content": "Levítico 11: Quais as regras dos alimentos considerados comestíveis e não comestíveis.",
                    "subRequirementTypeId": 1
                }
            ]
        },
        {
            "content": "Ler e explicar os versos abaixos:",
            "requirementGroupId": 2,
            "classId": 3,
            "subRequirements": [
                {
                    "content": "Ecles. 12:13-14",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Rom. 6:23",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Apoc. 1:3",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Isa. 43:1-2",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Salmo 51:10",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Salmo 16",
                    "subRequirementTypeId": 1
                }
            ]
        },
        {
            "content": "Leitura bíblica:",
            "requirementGroupId": 2,
            "classId": 3,
            "suRequirements": [
                {
                    "content": "1 Rs 1:28-53, 3, 4:20-34, 5, 6, 8:12-60, 10, 11:6-43, 12, 16:29-33, 17:1-7, 17:8-24, 18, 19, 21",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "2 Rs 2, 4:1-7, 4:8-41, 5, 6:1-23, 6:24-33, 7, 20, 22, 23:36-37, 24, 25:1-7",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "2 Cr 24:1-14, 36",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "Ed 1, 3, 6:14-15",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "Ne 1, 2, 4, 8",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "Ester 1, 2, 3, 4, 5, 6, 7, 8",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "Jó 1, 2, 42",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "Sl 1, 15, 19, 23, 24, 27, 37, 39, 42, 46, 67, 90, 91, 92, 97, 98, 100, 117, 119:1-176, 121, 125, 150",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "Pv 1, 3, 4, 10, 15, 20, 25",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "Ec 1",
                    "subRequirementTypeId": 2
                }
            ]
        },
        {
            "content": "Conversar com seu líder e escolher uma das seguintes histórias:",
            "requirementGroupId": 2,
            "classId": 3,
            "subRequirements": [
                {
                    "content": "João 3 - Nicodemos",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "João 4 - A mulher samaritana",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Lucas 10 - O bom samaritano",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Lucas 19 - Zaqueu",
                    "subRequirementTypeId": 1
                }
            ]
        },
        {
            "content": "Através da história escolhida, demonstrar sua compreensão em como Jesus salva as pessoas, usando um dos métodos abaixo.",
            "requirementGroupId": 2,
            "classId": 3,
            "subRequirements": [
                {
                    "content": "Conversar em grupo com a participação de seu líder",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Apresentar uma mensagem em uma reunião do Clube",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Fazer uma série de cartazes ou uma maquete",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Escrever uma poesia ou hino",
                    "subRequirementTypeId": 1
                }
            ]
        },
        {
            "content": "Conhecer os projetos comunitários desenvolvidos em sua cidade e participar em pelo menos um deles com sua unidade ou Clube.",
            "requirementGroupId": 3,
            "classId": 3
        },
        {
            "content": "Participar em três atividades missionárias da igreja.",
            "requirementGroupId": 3,
            "classId": 3
        },
        {
            "content": "Participar de um debate ou representação sobre a pressão de grupo e identificar a influência que isto exerce sobre suas decisões.",
            "requirementGroupId": 4,
            "classId": 3
        },
        {
            "content": "Visitar um órgão público de sua cidade ou bairro e descobrir de que maneiras o clube pode ser útil à sua comunidade.",
            "requirementGroupId": 4,
            "classId": 3
        },
        {
            "content": "Escolher uma das atividades abaixo e escrever um texto pessoal par aum estilo de vida livre do álcool:",
            "requirementGroupId": 5,
            "classId": 3,
            "subRequirements": [
                {
                    "content": "Participar de uma discussão em classe sobre os efeitos do álcool no organismo.",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Assistir a um vídeo sobre o efeito do álcool ou outras drogas no corpo humano e conversar sobre o assunto.",
                    "subRequirementTypeId": 1
                }
            ]
        },
        {
            "content": "Dirigir uma cerimônia de abertura da reunião semanal em seu clube ou um programa de Escola Sabatina.",
            "requirementGroupId": 6,
            "classId": 3
        },
        {
            "content": "Ajudar a organizar a classe bíblica do seu clube.",
            "requirementGroupId": 6,
            "classId": 3
        },
        {
            "content": "Identificar a estrela Alfa da constelação do Centauro e a constelação de Ório. Conhecer o significado espiritual de Ório, como descrito no livro Primeiros Escritos, de Ellen White, pág. 41.",
            "requirementGroupId": 7,
            "classId": 3
        },
        {
            "content": "Completar uma das especialidades a seguir:",
            "requirementGroupId": 7,
            "classId": 3,
            "subRequirements": [
                {
                    "content": "Astronomia",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Cactos",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Climatologia",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Flores",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Rastreio de animais",
                    "subRequirementTypeId": 1
                }
            ]
        },
        {
            "content": "Apresentar seis segredos para um bom acampamento. Participar de um acampamento de final de semana, planejando e cozinhando duas refeições.",
            "requirementGroupId": 8,
            "classId": 3
        },
        {
            "content": "Completar as seguintes especialidades.",
            "requirementGroupId": 8,
            "classId": 3,
            "subRequirements": [
                {
                    "content": "Acampamento 3",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Primeiros socorros - básico",
                    "subRequirementTypeId": 1
                }
            ]
        },
        {
            "content": "Aprender a usar uma bússola ou um GPS (urbano ou campo), e demonstrar sua habilidade encontrando endereços em uma zona urbana.",
            "requirementGroupId": 8,
            "classId": 3
        },
        {
            "content": "Completar uma especialidade, não realizada anteriormente, em Artes e habilidades manuais.",
            "requirementGroupId": 9,
            "classId": 3
        },
        {
            "content": "Conhecer e saber usar de forma adequada a bandeira dos Desbravadores e o bandeirim de unidade e os comandos de ordem unida.",
            "requirementGroupId": 10,
            "classId": 3
        },
        {
            "content": "Ler a história de J. N. Andrews ou um pioneiro de seu país e discutir a importância do trabalho de missionários, e por que Cristo ordenou a Grande Comissão (Mateus 28:18-20).",
            "requirementGroupId": 10,
            "classId": 3
        },
        {
            "content": "Convidar uma pessoa para assitir um dos seguintes programas:",
            "requirementGroupId": 10,
            "classId": 3,
            "subRequirements": [
                {
                    "content": "Clube de Desbravadores",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Classe bíblica",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Pequenos grupos",
                    "subRequirementTypeId": 1
                }
            ]
        },
        {
            "content": "Fazer uma das seguintes especialidades:",
            "requirementGroupId": 10,
            "classId": 3,
            "subRequirements": [
                {
                    "content": "Asseio e cortesia cristã",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Vida familiar",
                    "subRequirementTypeId": 1
                }
            ]
        },
        {
            "content": "Participar de uma caminhada de 10 quilômetros e fazer uma lista dos equipamentos necessários, incluindo a roupa e o calçado que devem ser usados.",
            "requirementGroupId": 10,
            "classId": 3
        },
        {
            "content": "Participar na organização d eum dos eventos especiais do Clube:",
            "requirementGroupId": 10,
            "classId": 3,
            "subRequirements": [
                {
                    "content": "investidura",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Admissão em lenço",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Dia Mundial do Desbravador",
                    "subRequirementTypeId": 1
                }
            ]
        },
        {
            "content": "Identificar seis pegadas de animais ou aves. Fazer um modelo em gesso, massa de modelar ou biscuit de três dessas pegadas.",
            "requirementGroupId": 10,
            "classId": 3
        },
        {
            "content": "Aprender a fazer as quatro amarras básicas e construir um móvel de acampamento.",
            "requirementGroupId": 10,
            "classId": 3
        },
        {
            "content": "Planejar um cardápio vegetariano para sua unidade, para um acampamento de 3 dias e apresentar ao seu instrutor.",
            "requirementGroupId": 10,
            "classId": 3
        },
        {
            "content": "Enviar e receber uma mensagem através das formas de comunicação abaixo:",
            "requirementGroupId": 10,
            "classId": 3,
            "subRequirements": [
                {
                    "content": "Alfabeto com semáforos",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Código Morse, com lanterna",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Alfabeto LIBRAS (língua brasileira de sinais)",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Alfabeto Braile",
                    "subRequirementTypeId": 1
                }
            ]
        },
        {
            "content": "Completar duas especialidades, não realizadas anteriormente, em uma das áreas abaixo:",
            "requirementGroupId": 10,
            "classId": 3,
            "subRequirements": [
                {
                    "content": "Habilidades domésticas",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Ciência e saúde",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Atividades missionárias e comunitárias",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Atividades agrícolas e afins",
                    "subRequirementTypeId": 1
                }
            ]
        }
    ]
}

pioneer_requirements = {
    "requirements": [
        {
            "content": "Ter, no mínimo, 13 anos de idade.",
            "requirementGroupId": 1,
            "classId": 4
        },
        {
            "content": "Ser membro ativo do Clube de Desbravadores.",
            "requirementGroupId": 1,
            "classId": 4
        },
        {
            "content": "Memorizar e entender o Alvo e o Lema JA.",
            "requirementGroupId": 1,
            "classId": 4
        },
        {
            "content": "Ler o livro do Clube de Leitura do ano em curso e resumi-lo em uma página.",
            "requirementGroupId": 1,
            "classId": 4
        },
        {
            "content": "Ler o livro a história da vida.",
            "requirementGroupId": 1,
            "classId": 4
        },
        {
            "content": "Memorizar e demonstrar o seu conhecimento:",
            "requirementGroupId": 2,
            "classId": 4,
            "subRequirements": [
                {
                    "content": "Bem-Aventuranças: O Sermão da Montanha.",
                    "subRequirementTypeId": 1
                }
            ]
        },
        {
            "content": "Ler e explicar os versos abaixo:",
            "requirementGroupId": 2,
            "classId": 4,
            "subRequirements": [
                {
                    "content": "Isa. 26:3",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "Rom. 12:12",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "João 14:1-3",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "Sal. 37:5",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "Filip. 3:12-14",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "Salmo 23",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "1 Sam. 15:22",
                    "subRequirementTypeId": 2
                }
            ]
        },
        {
            "content": "Conversar em seu clube ou unidade sobre:",
            "requirementGroupId": 2,
            "classId": 4,
            "subRequirements": [
                {
                    "content": "O que é o cristianismo",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Quais são as características de um verdadeiro discípulo",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "O que fazer para ser um cristão verdadeiro",
                    "subRequirementTypeId": 1
                }
            ]
        },
        {
            "content": "Participar de um estudo especial sobre a inspiração da Bíblia, com a ajuda de um pastor, trabalhando os conceitos de inspiração, revelação e iluminação.",
            "requirementGroupId": 2,
            "classId": 4
        },
        {
            "content": "Convidar três ou mais pessoas para assistirem a uma classe bíblica ou pequeno grupo.",
            "requirementGroupId": 2,
            "classId": 4
        },
        {
            "content": "Leitura Bíblica:",
            "requirementGroupId": 2,
            "classId": 2,
            "subRequirements": [
                {
                    "content": "Ec 3, 5, 7, 11 e 12",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "Is 5, 11, 26:1-12, 35, 40, 43, 52:13-15, 53, 58, 60, 61",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "Jr 9:23-26, 10:1-16, 18:1-6, 26, 36, 52:1-11",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "Dn 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "Jl 2:12-31",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "Am 7:10-16, 8:4-11",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "Jn 1, 2, 3 e 4",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "Mq 4",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "Ag 2",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "Zc 4",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "Ml 3 e 4",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "Mt 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23",
                    "subRequirementTypeId": 2
                },
            ]
        },
        {
            "content": "Participar em dois projetos missionários definidos por seu Clube.",
            "requirementGroupId": 3,
            "classId": 4
        },
        {
            "content": "Trabalhar em um projeto comunitário de sua igreja, escola ou comunidade.",
            "requirementGroupId": 3,
            "classId": 4
        },
        {
            "content": "Participar de um debate e fazer uma avaliação pessoal sobre suas atitudes em dois dos seguintes temas:",
            "requirementGroupId": 4,
            "classId": 4,
            "subRequirements": [
                {
                    "content": "Autoestima",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Amizade",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Relacionamentos",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Otimismo e pessimismo",
                    "subRequirementTypeId": 1
                },
            ]
        },
        {
            "content": "Preparar um programa pessoal de exercícios físicos diários e conversar com seu líder ou conselheiro sobre os princípios de aptidão física. Fazer e assinar um compromisso pessoal de realizar exercícios físicos regularmente.",
            "requirementGroupId": 5,
            "classId": 4
        },
        {
            "content": "Discutir as vantagens do estilo de vida adventista de acordo com o que a Bíblia ensina.",
            "requirementGroupId": 5,
            "classId": 4
        },
        {
            "content": "Assistir a um seminário ou treinamento, oferecido pela sua igreja ou distrito nos departamentos abaixo:",
            "requirementGroupId": 6,
            "classId": 4,
            "subRequirements": [
                {
                    "content": "Ministério Pessoal",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Evangelismo",
                    "subRequirementTypeId": 1
                }
            ]
        },
        {
            "content": "Participar de uma atividade social de sua igreja.",
            "requirementGroupId": 6,
            "classId": 4
        },
        {
            "content": "Estudar a história do dilúvio e estudar o processo de fossilização.",
            "requirementGroupId": 7,
            "classId": 4
        },
        {
            "content": "Completar uma especialidade, não realizada anteriormente, em Estudo da natureza.",
            "requirementGroupId": 7,
            "classId": 4
        },
        {
            "content": "Fazer um fogo refletor e demonstrar seu uso.",
            "requirementGroupId": 8,
            "classId": 4
        },
        {
            "content": "Participar de um acampamento de final de semana, arrumando de forma apropriada sua bolsa ou mochila com o equipamento pessoal necessário.",
            "requirementGroupId": 8,
            "classId": 4
        },
        {
            "content": "Completar a especialidade de Resgate básico.",
            "requirementGroupId": 8,
            "classId": 4
        },
        {
            "content": "Completar uma especialidade não realizada anteriormente em uma das seguintes áreas:",
            "requirementGroupId": 9,
            "classId": 4,
            "subRequirements": [
                {
                    "content": "Atividades missionárias e comunitárias",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Atividades profissionais",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Atividades agrícolas e afins",
                    "subRequirementTypeId": 1
                }
            ]
        },
        {
            "content": "Completar a especialidade de Cidadania cristã, caso não tenha sido realizada anteriormente.",
            "requirementGroupId": 10,
            "classId": 4
        },
        {
            "content": "Dar dois estudos bíblicos a uma pessoa não batizada na Igreja Adventista.",
            "requirementGroupId": 10,
            "classId": 4
        },
        {
            "content": "Encenar a história do bom samaritano, demonstrando como ajudar as pessoas e auxiliar de forma prática três pessoas ou mais.",
            "requirementGroupId": 10,
            "classId": 4
        },
        {
            "content": "Participar de uma das seguintes atividades, apresentando ao final um relatório escrito contendo no mínimo duas páginas:",
            "requirementGroupId": 10,
            "classId": 4,
            "subRequirements": [
                {
                    "content": "Caminhar 10 quilômetros",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Cavalgar 2 quilômetros",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Viajar de canoa durante 2 horas",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Praticar 15 quilômetros de ciclismo",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Nadar 200 metros",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Correr 1500m",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Rodar 2 km de patins ou roller",
                    "subRequirementTypeId": 1
                }
            ]
        },
        {
            "content": "Completar a especialidade de Mapa e bússola.",
            "requirementGroupId": 10,
            "classId": 4
        },
        {
            "content": "Demonstrar habilidade no uso correto de uma machadinha.",
            "requirementGroupId": 10,
            "classId": 4
        },
        {
            "content": "Ser capaz de acender uma fogueira em dia de chuva, saber como conseguir lenha seca e manter o fogo aceso.",
            "requirementGroupId": 10,
            "classId": 4
        },
        {
            "content": "Completar um dos seguintes itens:",
            "requirementGroupId": 10,
            "classId": 4,
            "subRequirements": [
                {
                    "content": "Pesquisar e identificar dez variedades de plantas silvestres comestíveis.",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Ser capaz de enviar e receber 35 letras por minuto pelo código semafórico.",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Ser capaz de enviar e receber 35 letras por minuto através do código náutico, usando o código internacional.",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Ser capaz de apresentar e entender Mateus 24 em LIBRAS (língua brasileira de sinais).",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Preparar o salmo 23 em braile.",
                    "subRequirementTypeId": 1
                }
            ]
        },
        {
            "content": "Completar uma especialidade, não realizada anteriormente, em Atividades recreativas.",
            "requirementGroupId": 10,
            "classId": 4
        },
        {
            "content": "Pesquisar e identificar, através de fotografia, exposição ou ao vivo, um dos seguintes itens:",
            "requirementGroupId": 10,
            "classId": 4,
            "subRequirements": [
                {
                    "content": "25 folhas de árvores",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "25 rochas e minerais",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "25 flores silvestres",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "25 borboletas e mariposas",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "25 conchas",
                    "subRequirementTypeId": 1
                }
            ]
        },
        {
            "content": "Completar a especialidade de Fogueiras e cozinha ao ar livre.",
            "requirementGroupId": 10,
            "classId": 4
        }
    ]
}

hiker_requirements = {}

guide_requirements = {}

def populate_db(connection, db_data):
    try:
        print("inserindo requisitos...")

        requirements = db_data["requirements"]

        cursor = connection.cursor()

        for requirement in requirements:
            requirement_content = requirement["content"]
            requirement_group_id = requirement["requirementGroupId"]
            requirement_class_id = requirement["classId"]
            sub_requirements = requirement.get("subRequirements")

            print("inserindo requisito:")
            print(f"conteúdo do requisito: {requirement_content}")
            print(f"grupo do requisito: {requirement_group_id}")
            print(f"classe do requisito: {requirement_class_id}")

            sql = """
                insert into requirement (content, requirementGroupId, classId)
                values (%s, %s, %s);
            """

            values = (requirement_content, requirement_group_id, requirement_class_id)

            cursor.execute(sql, values)

            requirement_id = cursor.lastrowid

            if sub_requirements is not None:
                for sub_requirement in sub_requirements:
                    sub_requirement_content = sub_requirement["content"]
                    sub_requirement_type_id = sub_requirement["subRequirementTypeId"]

                    sql = """
                        insert into subRequirement (content, subRequirementTypeId, requirementId)
                        values (%s, %s, %s);
                    """

                    values = (sub_requirement_content, sub_requirement_type_id, requirement_id)

                    cursor.execute(sql, values)

        
        connection.commit()

        cursor.close()

        connection.close()
    
    except Exception as err:
        connection.rollback()

        _, _, exc_tb = sys.exc_info()

        print(f"Erro encontrado:\n\n\n{err._full_msg}")
        print(f"error line: {exc_tb.tb_lineno}")


populate_db(connection, pioneer_requirements)
