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

hiker_requirements = {
    "requirements": [
        {
            "content": "Ter, no mínimo, 14 anos de idade.",
            "requirementGroupId": 1,
            "classId": 5
        },
        {
            "content": "Ser membro ativo do Clube de Desbravadores.",
            "requirementGroupId": 1,
            "classId": 5
        },
        {
            "content": "Memorizar e explicar o significado do Objetivo JA.",
            "requirementGroupId": 1,
            "classId": 5
        },
        {
            "content": "Ler o livro do Clube de Leitura do ano em curso e resumi-lo em uma página.",
            "requirementGroupId": 1,
            "classId": 5
        },
        {
            "content": "Ler o livro Nos bastidores da mídia.",
            "requirementGroupId": 1,
            "classId": 5
        },
        {
            "content": "Memorizar e demonstrar o seu conhecimento:",
            "requirementGroupId": 2,
            "classId": 5,
            "subRequirements": [
                {
                    "content": "12 Apóstolos: O nome dos 12 apóstolos de Cristo.",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "O Fruto do Espírito: A relação de adjetivos do caráter do cristão.",
                    "subRequirementTypeId": 1
                }
            ]
        },
        {
            "content": "Memorizar e recitar os versos abaixo:",
            "requirementGroupId": 2,
            "classId": 5,
            "subRequirements": [
                {
                    "content": "Rom. 12:12",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "Apoc. 21:1-3",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "2 Ped. 1:20-21",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "1 João 2:14",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "2 Cro. 20:20",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "Salmo 46",
                    "subRequirementTypeId": 2
                }
            ]
        },
        {
            "content": "Estudar e entender a pessoa do Espírito Santo, como Ele se relaciona, e qual o Seu papel no crescimento espiritual de cada ser humano.",
            "requirementGroupId": 2,
            "classId": 5
        },
        {
            "content": "Estude, com a sua unidade, os eventos finais e a segunda vinda de Cristo.",
            "requirementGroupId": 2,
            "classId": 5
        },
        {
            "content": "Através do estudo da Bíblia, descobrir o verdadeiro significado da observância do sábado.",
            "requirementGroupId": 2,
            "classId": 5
        },
        {
            "content": "Leitura bíblica",
            "requirementGroupId": 2,
            "classId": 5,
            "subRequirements": [
                {
                    "content": "Mt 24, 25, 26:1-35, 26:36-75, 27:1-31, 27:32-56, 27:57-66, 28",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Mc 7, 9, 10, 11, 12, 16",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Lc 1:4-25, 1:26-66, 2:21-38, 2:39-52, 7:18-28, 8, 10:1-37, 10:38-42, 11:1-13, 12, 13, 14, 15, 16:1-17, 17, 18, 19, 21, 22, 23, 24",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Jo 1, 2, 3, 4, 5, 6:1-21, 6:22-71, 8:1-38, 9, 10, 11:1-46, 12, 13, 14, 15, 17, 18, 19, 20, 21",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "At 1, 2, 3, 4, 5, 6, 7, 8",
                    "subRequirementTypeId": 1
                },
            ]
        },
        {
            "content": "Convidar um amigo para participar de uma atividade social de sua igreja ou da Associação/Missão.",
            "requirementGroupId": 3,
            "classId": 5
        },
        {
            "content": "Participar de um projeto comunitário desde o planejamento, organização até a execução.",
            "requirementGroupId": 3,
            "classId": 5
        },
        {
            "content": "Discutir como os jovens adventistas devem se relacionar com as pessoas nas diferentes situações do dia a dia, tais como:",
            "requirementGroupId": 3,
            "classId": 5,
            "subRequirements": [
                {
                    "content": "Vizinhança",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Escola",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Atividades sociais",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Atividades recreativas",
                    "subRequirementTypeId": 1
                }
            ]
        },
        {
            "content": "Através de uma conversa em grupo ou avaliação pessoal, examinar suas atitudes em dois dos seguintes temas:",
            "requirementGroupId": 4,
            "classId": 5,
            "subRequirements": [
                {
                    "content": "Autoestima.",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Relacionamento familiar.",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Finanças pessoais.",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Pressão de grupo.",
                    "subRequirementTypeId": 1
                }
            ]
        },
        {
            "content": "Preparar uma lista contendo cinco sugestões de atividades recreativas para ajudar pessoas com necessidades específicas e colaborar na organização d euma atividade para essas pessoas.",
            "requirementGroupId": 4,
            "classId": 5
        },
        {
            "content": "Completar a especialidade de Temperança.",
            "requirementGroupId": 5,
            "classId": 5
        },
        {
            "content": "Preparar um organograma da igreja local e relacionar as funções dos departamentos.",
            "requirementGroupId": 6,
            "classId": 5
        },
        {
            "content": "Participar de dois programas envolvendo diferentes departamentos da igreja local.",
            "requirementGroupId": 6,
            "classId": 5
        },
        {
            "content": "Completar a especialidade de Aventuras com Cristo.",
            "requirementGroupId": 6,
            "classId": 5
        },
        {
            "content": "Recapitular a história de Nicodemos e relacioná-la com o ciclo de vida da lagarta ou borboleta, acrescentando um significado espiritual.",
            "requirementGroupId": 7,
            "classId": 5
        },
        {
            "content": "Completar uma especialidade em estudo da natureza, não realizada anteriormente.",
            "requirementGroupId": 7,
            "classId": 5
        },
        {
            "content": "Com um grupo de, no mínimo, quatro pessoas e com a presença de um conselheiro adulto e experiente, andar pelo menos 20 quilômetros numa área rural ou deserta, incluindo uma noite ao ar livre ou em barraca. Planejar a expedição em detalhes antes da saída. Durante a caminhada, efetuar anotações sobre o terreno, flora e fauna observados. Depois, usando as anotações, participar de uma discussão em grupo, dirigida por seu conselheiro.",
            "requirementGroupId": 8,
            "classId": 5
        },
        {
            "content": "Completar a especialidade de Pioneirias.",
            "requirementGroupId": 8,
            "classId": 5
        },
        {
            "content": "Completar uma especialidade não realizada anteriormente em uma das seguintes áreas:",
            "requirementGroupId": 9,
            "classId": 5,
            "subRequirements": [
                {
                    "content": "Atividades missionárias e comunitárias",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Atividades agrícolas e afins",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Ciência e saúde",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Habilidades domésticas",
                    "subRequirementTypeId": 1
                }
            ]
        },
        {
            "content": "Fazer uma apresentação escrita ou falada sobre o respeito que devemos ter com a Lei de Deus e as autoridades civis, enumerando 10 princípios de comportamento moral.",
            "requirementGroupId": 10,
            "classId": 5
        },
        {
            "content": "Acompanhar seu pastor ou ancião numa visita missionária ou estudo bíblico.",
            "requirementGroupId": 10,
            "classId": 5
        },
        {
            "content": "Completar a especialidade de Testemunho juvenil.",
            "requirementGroupId": 10,
            "classId": 5
        },
        {
            "content": "Apresentar cinco atividades na natureza, para serem realizadas no sábado à tarde.",
            "requirementGroupId": 10,
            "classId": 5
        },
        {
            "content": "Com sua unidade, construir cinco móveis de acampamento e um portal para o clube.",
            "requirementGroupId": 10,
            "classId": 5
        },
        {
            "content": "Sob a supervisão de seu líder ou conselheiro, conversar em sua unidade ou clube sobre um dos seguintes temas:",
            "requirementGroupId": 10,
            "classId": 5,
            "subRequirements": [
                {
                    "content": "Modéstia cristã.",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Recreação.",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Saúde.",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Observância do sábado.",
                    "subRequirementTypeId": 1
                }
            ]
        },
        {
            "content": "Demonstrar conhecimento para encontrar alimentos, através de plantas silvestres de sua região e saber diferenciá-las de plantas tóxicas/venenosas.",
            "requirementGroupId": 10,
            "classId": 5
        },
        {
            "content": "Demonstrar conhecimento quanto aos procedimentos necessários em caso de ferimentos por diferentes animais peçonhentos e não peçonhentos.",
            "requirementGroupId": 10,
            "classId": 5
        },
        {
            "content": "Demonstrar técnicas para percorrer trilhas em diferentes tipos de terrenos, como: desertos, florestas, pântanos e rios.",
            "requirementGroupId": 10,
            "classId": 5
        },
        {
            "content": "Completar a especialidade de Ordem unida, caso não tenha sido realizada anteriormente.",
            "requirementGroupId": 10,
            "classId": 5
        },
        {
            "content": "Completar a especialidade de Vida silvestre.",
            "requirementGroupId": 10,
            "classId": 5
        },
    ]
}

guide_requirements = {
    "requirements": [
        {
            "content": "Ter, no mínimo, 15 anos de idade.",
            "requirementGroupId": 1,
            "classId": 6
        },
        {
            "content": "Ser membro ativo do Clube de Desbravadores.",
            "requirementGroupId": 1,
            "classId": 6
        },
        {
            "content": "Memorizar e explicar o Voto de Fidelidade à Bíblia.",
            "requirementGroupId": 1,
            "classId": 6
        },
        {
            "content": "Ler o livro do Clube de Leitura do ano em curso e resumi-lo em uma página",
            "requirementGroupId": 1,
            "classId": 6
        },
        {
            "content": "Ler o livro Nossa Herança.",
            "requirementGroupId": 1,
            "classId": 6
        },
        {
            "content": "Memorizar e demonstrar o seu conhecimento:",
            "requirementGroupId": 2,
            "classId": 6,
            "subRequirements": [
                {
                    "content": "As 3 Mensagens Angélicas: Reveladas em Apocalipse 14:6-12.",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "7 Igrejas: O nome das igrejas do Apocalipse.",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Pedras preciosas: Quais as pedras preciosas dos 12 fundamentos da cidade santa - a nova Jerusalém.",
                    "subRequirementTypeId": 1
                },
            ]
        },
        {
            "content": "Ler e explicar os versos abaixo:",
            "requirementGroupId": 2,
            "classId": 6,
            "subRequirements": [
                {
                    "content": "1 Cor. 13",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "2 Cron. 7:14",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "Apoc. 22:18-20",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "2 Tim. 4:6-7",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "Rom. 8:38-39",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "Mateus 6:33-34",
                    "subRequirementTypeId": 2
                },
            ]
        },
        {
            "content": "Descrever os dons espirituais mencionados nos de Paulo (Coríntios, Efésios, Filipenses) e para que a igreja recebe estes dons.",
            "requirementGroupId": 2,
            "classId": 6
        },
        {
            "content": "Estudar a estrutura e serviço do santuário no Antigo Testamento e relacionar com o ministério pessoal de Jesus e a cruz.",
            "requirementGroupId": 2,
            "classId": 6
        },
        {
            "content": "Ler e reunir três histórias de pioneiros adeventistas. Contar estas histórias na reunião do Clube, no culto JA ou na escola sabatina.",
            "requirementGroupId": 2,
            "classId": 6
        },
        {
            "content": "Leitura bíblica:",
            "requirementGroupId": 2,
            "classId": 6,
            "subRequirements": [
                {
                    "content": "At 9:1-31, 9:32-43, 10, 11, 12, 13, 14, 16, 17:1-15, 17:16-34, 18, 19:1-22, 19:23-41, 20, 21:17-40, 22:1-16, 23, 24, 25, 26, 27, 28",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "Rm 12, 13, 14",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "1 Co 13",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "2 Co 5:11-21, Co 11:16-33, 12:1-10",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "Gl 5:16-26, 6:1-10",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "Ef 5:1-21, 6",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "Fp 4",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "Cl 3",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "1 Ts 4:13-18, 5",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "2 Ts 2, 3",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "1 Tm 4:6-16, Tm 5:1-16, 6:11-21",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "2 Tm 2, 3",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "Fm",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "Hb 11",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "Tg 1, 3, 5:7-20",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "1 Pe 1, 5:1-11",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "1 Pe 3",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "1 Jo 2, 3, 4, 5",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "Jd 1:17-25",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "Ap 1, 2, 3, 7:9-17, 12, 13, 14, 19, 20, 21",
                    "subRequirementTypeId": 2
                }
            ]
        },
        {
            "content": "Ajudar a organizar e participar de uma das seguintes atividades:",
            "requirementGroupId": 3,
            "classId": 6,
            "subRequirements": [
                {
                    "content": "Fazer uma visita de cortesia a uma pessoa doente.",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "Adotar uma pessoa ou família em necessidade.",
                    "subRequirementTypeId": 2
                },
                {
                    "content": "Um projeto de sua escolha aprovado por seu líder.",
                    "subRequirementTypeId": 2
                },
            ]
        },
        {
            "content": "Discutir com sua unidade os métodos de evangelismo pessoal e colocar alguns princípios em prática.",
            "requirementGroupId": 3,
            "classId": 6
        },
        {
            "content": "Asitir a uma palestra ou aula e examinar suas atitudes em relação a dois dos seguintes temas:",
            "requirementGroupId": 4,
            "classId": 6,
            "subRequirements": [
                {
                    "content": "A importância da escolha profissional.",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Como se relacionar com os pais.",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "A escolha da pessoa certa para namorar.",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "O plano de Deus para o sexo.",
                    "subRequirementTypeId": 1
                }
            ]
        },
        {
            "content": "Fazer uma apresentação, para os alunos do ensino fundamental, sobre os oito remédios naturais dados por Deus.",
            "requirementGroupId": 5,
            "classId": 6
        },
        {
            "content": "Completar uma das seguintes atividades:",
            "requirementGroupId": 5,
            "classId": 6,
            "subRequirements": [
                {
                    "content": "Escrever uma poesia ou artigo sobre saúde para ser divulgado em uma revista, boletim ou jornal da igreja.",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Individualmente ou em grupo, organizar e participar de uma corrida ou atividade similar e apresentar com antecedência um programa de treinamento físico para este evento.",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Ler as páginas 102-125 do livro Temperança, de Ellen White, e apresentar em uma página ou mais, 10 textos selecionados da leitura.",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Completar a especialidade de Nutrição ou liderar um gurpo para a especialidade de Cultura física.",
                    "subRequirementTypeId": 1
                }
            ]
        },
        {
            "content": "Preparar um organograma da estrutura administrativa da Igreja Adventista em sua Divisão.",
            "requirementGroupId": 6,
            "classId": 6
        },
        {
            "content": "Participar em um dos itens abaixo:",
            "requirementGroupId": 6,
            "classId": 6,
            "subRequirements": [
                {
                    "content": "Curso para conselheiros",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Convenção de liderança da Associação/Missão",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "6 reuniões de diretoria do seu Clube",
                    "subRequirementTypeId": 1
                }
            ]
        },
        {
            "content": "Planejar e ensinar, no mínimo, dois requisitos de uma especialidade para um grupo ou unidade de desbravadores.",
            "requirementGroupId": 6,
            "classId": 6
        },
        {
            "content": "Ler o capítulo 7 do livro O Desejado de Todas as Nações sobre a infância de Jesus. Apresentar para um grupo, clube ou unidades as lições encontradas, desmonstrando a importância que o estudo da natureza e ministêrio de Jesus.",
            "requirementGroupId": 7,
            "classId": 6
        },
        {
            "content": "Completar uma das seguintes especialidades:",
            "requirementGroupId": 7,
            "classId": 6,
            "subRequirements": [
                {
                    "content": "Ecologia.",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Conservação ambiental.",
                    "subRequirementTypeId": 1
                }
            ]
        },
        {
            "content": "Participar com sua unidade de um acampamento com estrutura de pioneiria, planejar o que deve ser levado e o que vai acontecer neste acampamento.",
            "requirementGroupId": 8,
            "classId": 6
        },
        {
            "content": "Planejar, preparar e cozinhar três refeições ao ar livre.",
            "requirementGroupId": 8,
            "classId": 6
        },
        {
            "content": "Construir e utilizar um móvel de acampamento em tamanho real, com nós e amarras.",
            "requirementGroupId": 8,
            "classId": 6
        },
        {
            "content": "Completar uma especialidade, não realizada anteriormente, que possa ser contada para um dos Mestrados a seguir:",
            "requirementGroupId": 8,
            "classId": 6,
            "subRequirements": [
                {
                    "content": "Aquática",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Esportes",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Atividades recreativas",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Vida campestre",
                    "subRequirementTypeId": 1
                }
            ]
        },
        {
            "content": "Completar uma especialidade, não realizada anteriormente, em uma das seguintes áreas:",
            "requirementGroupId": 9,
            "classId": 6,
            "subRequirements": [
                {
                    "content": "Atividades recreativas",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Ciência e saúde",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Habilidades domésticas",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Atividades profissionais",
                    "subRequirementTypeId": 1
                }
            ]
        },
        {
            "content": "Completar a especialidade de Mordomia.",
            "requirementGroupId": 10,
            "classId": 6
        },
        {
            "content": "Ler o livro O Maior Discurso de Cristo e escrever uma página sobre o efeito da leitura em sua vida.",
            "requirementGroupId": 10,
            "classId": 6
        },
        {
            "content": "Cumprir um dos seguintes itens:",
            "requirementGroupId": 10,
            "classId": 6,
            "subRequirements": [
                {
                    "content": "Trazer dois amigos para assistir a duas diferentes reuniões da igreja.",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Ajudar a planejar e participar de, no mínimo, quatro domingos em uma série de evangelismo jovem.",
                    "subRequirementTypeId": 1
                }
            ]
        },
        {
            "content": "Escrever uma página ou apresentar uma palestra de como influenciar amigos para Cristo.",
            "requirementGroupId": 10,
            "classId": 6
        },
        {
            "content": "Observar durante o período de dois meses o trabalho dos diáconos, apresentando um relatório detalhado de suas atividades, contendo:",
            "requirementGroupId": 10,
            "classId": 6,
            "subRequirements": [
                {
                    "content": "Cuidado da propriedade da igreja",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Cerimônia de lava-pés",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Cerimônia de batismo",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Recolhimento dos dízimos e ofertas",
                    "subRequirementTypeId": 1
                }
            ]
        },
        {
            "content": "Completar o mestrado em Vida campestre.",
            "requirementGroupId": 10,
            "classId": 6
        },
        {
            "content": "Projetar três tipos diferentes de abrigo, explicar seu uso e utilizar um deles em um acampamento.",
            "requirementGroupId": 10,
            "classId": 6
        },
        {
            "content": "Assistir a um seminário ou apresentar uma palestra sobre dois dos seguintes temas:",
            "requirementGroupId": 10,
            "classId": 6,
            "subRequirements": [
                {
                    "content": "Aborto",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Builling",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Violência",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Drogas",
                    "subRequirementTypeId": 1
                },
                {
                    "content": "Doenças sexualmente transmissíveis",
                    "subRequirementTypeId": 1
                }
            ]
        },
        {
            "content": "Completar a especialidade de Liderança campestre.",
            "requirementGroupId": 10,
            "classId": 6
        },
        {
            "content": "Completar a especialidade de Orçamento familiar.",
            "requirementGroupId": 10,
            "classId": 6
        }
    ]
}

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
            print(f"\tconteúdo do requisito: {requirement_content}")
            print(f"\tgrupo do requisito: {requirement_group_id}")
            print(f"\tclasse do requisito: {requirement_class_id}")

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


populate_db(connection, guide_requirements)
