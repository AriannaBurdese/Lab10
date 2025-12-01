from flet.core import row

from database.DB_connect import DBConnect
from model.hub import Hub
from model.spedizione import Spedizione
from model.tratta import Tratta


class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """
    @staticmethod
    def read_all_edges() -> list[Tratta] | None:
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("❌ Errore di connessione al database.")
            return None
        cursor = cnx.cursor(dictionary=True)
        query = ("""SELECT  LEAST(spedizione.id_hub_origine, spedizione.id_hub_destinazione) AS id_hub1,
                            GREATEST(spedizione.id_hub_origine, spedizione.id_hub_destinazione) AS id_hub2,
                            AVG(valore_merce) as media_valore_merce
                    FROM  spedizione
                    GROUP BY id_hub1, id_hub2 """)
        try:
            cursor.execute(query)
            for row in cursor:

                tratta = Tratta(
                    id_hub_origine = row["id_hub1"],
                    id_hub_destinazione = row["id_hub2"],
                    guadagno_medio= row["media_valore_merce"],

                )
                result.append(tratta)
        except Exception as e:
            print(f"Errore durante la query: {e}")
            result = None
        finally:
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def get_all_nodes() -> list[Hub] | None:
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("❌ Errore di connessione al database.")
            return None
        cursor = cnx.cursor(dictionary=True)
        query = ("""SELECT *
                    FROM hub""")
        try:
            cursor.execute(query)
            for row in cursor:

                hub = Hub(
                    id = row["id"],
                    codice =row["codice"],
                    nome =row["nome"],
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




