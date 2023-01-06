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

companion_requirements = {}

researcher_requirements = {}

pioneer_requirements = {}

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


populate_db(connection, db_data)
