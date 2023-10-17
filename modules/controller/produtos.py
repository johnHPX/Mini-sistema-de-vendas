from modules.model.sql import new_database

class Produtos():
    def __init__(self):
        pass


    def cadastrar(self, id:str, nome:str, preco:float, quantidade:int, descricao:str):
        try:
            conn = new_database()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO produtos (id, nome, preco, quantidade, descricao) VALUES (?,?,?,?,?)", (id, nome, preco, quantidade, descricao))
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)
        else:
            print('Cadastro criado com sucesso!')
        finally:
            print('Ação finalizada!')
        

    def listar(self)->list[dict]:
        try:
            conn = new_database()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM produtos")
            dto = list()
            for i in cursor.fetchall():
                obj = dict()
                obj['id'] = i[0]
                obj['nome'] = i[1]
                obj['preco'] = i[2]
                obj['quantidade'] = i[3]
                obj['descricao'] = i[4]
                dto.append(obj)
            conn.close()
        except Exception as e:
            print(e)
            return []
        else:
            return dto
        finally:
            print('Ação finalizada!')

    
    def buscar(self, id:str):
        try:
            conn = new_database()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM produtos WHERE id = ?", (id,))
            obj = dict()
            for i in cursor.fetchall():
                obj['id'] = i[0]
                obj['nome'] = i[1]
                obj['preco'] = i[2]
                obj['quantidade'] = i[3]
                obj['descricao'] = i[4]
            conn.close()
        except Exception as e:
            print(e)
            return {}
        else:
            return obj
        finally:
            print('Ação finalizada!')


    def editar(self, id:str, nome:str, preco:float, quantidade:int, descricao:str):
        try:
            conn = new_database()
            cursor = conn.cursor()
            cursor.execute("UPDATE produtos SET nome = ?, preco = ?, quantidade = ?, descricao = ? WHERE id = ?", (nome, preco, quantidade, descricao, id))
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)
        else:
            print('Produto editado com sucesso!')
        finally:
            print('Ação finalizada!')


    def remover(self, id:str):
        try:
            conn = new_database()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM produtos WHERE id = ?", (id,))
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)
        else:
            print('Produto removido com sucesso!')
        finally:
            print('Ação finalizada!')


def new_produtos():
    return Produtos()