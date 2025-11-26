from database.DB_connect import DBConnect
from model.hub import Hub


class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """
    @staticmethod
    def get_hub() -> list[Hub] | None:
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("❌ Errore di connessione al database.")
            return None
        cursor = cnx.cursor()
        query = ("""SELECT "
                    FROM  
                    
                    GROUP BY """)
        try:
            cursor.execute(query)
            for row in cursor:
                hub = Hub(
                    id = row["id"],
                    codice = row["codice"],
                    nome = row["nome"],
                    citta = row["citta"],
                    stato = row["stato"],
                    latitudine = row["latitudine"],
                    longitudine = row["longitudine"],
                )
                result.append(hub)
        except Exception as e:
            print(f"Errore durante la query: {e}")
            result = None
        finally:
            cursor.close()
            cnx.close()
        return result




