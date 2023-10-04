from modules.model.sql import new_database

class Vendedores():
    def __init__(self):
        pass


    def cadastrar(self, id:str, nome:str, data_nascimento:float):
        try:
            conn = new_database()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO vendedores (id, nome, data_nascimento) VALUES (?,?,?)", (id, nome, data_nascimento))
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
            cursor.execute("SELECT * FROM vendedores")
            dto = list()
            for i in cursor.fetchall():
                obj = dict()
                obj['id'] = i[0]
                obj['nome'] = i[1]
                obj['data_nascimento'] = i[2]
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
            cursor.execute("SELECT * FROM vendedores WHERE id = ?", (id,))
            obj = dict()
            for i in cursor.fetchall():
                obj['id'] = i[0]
                obj['nome'] = i[1]
                obj['data_nascimento'] = i[2]
            conn.close()
        except Exception as e:
            print(e)
            return {}
        else:
            return obj
        finally:
            print('Ação finalizada!')


    def editar(self, id:str, nome:str, data_nascimento:float):
        try:
            conn = new_database()
            cursor = conn.cursor()
            cursor.execute("UPDATE vendedores SET nome = ?, data_nascimento = ? WHERE id = ?", (nome,  id, data_nascimento))
            conn.commit()
            conn.close()
        except Exception as e:
            print(e)
        else:
            print('Vendedor editado com sucesso!')
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

