from database.DB_connect import DBConnect
from model.Gene import Gene
from model.interaction import Interaction


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllGenes():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT distinct g.GeneID as g1
            FROM genes g 
            WHERE g.Essential = 'Essential' """
            cursor.execute(query)

            for row in cursor:
                result.append(row["g1"])

            cursor.close()
            cnx.close()

        return result

    @staticmethod
    def getArchi():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT g1.GeneID as g1, g2.GeneID as g2, 
               i.Expression_Corr as peso, 
               g1.Chromosome as chr1, g2.Chromosome as chr2
        FROM genes g1, genes g2, interactions i 
        WHERE g1.Essential = 'Essential' 
          AND g2.Essential = 'Essential' 
          AND ((i.GeneID1 = g1.GeneID AND i.GeneID2 = g2.GeneID) 
               OR (i.GeneID1 = g2.GeneID AND i.GeneID2 = g1.GeneID))
            """
            cursor.execute(query)

            for row in cursor:
                peso = abs(row["peso"])
                if row["chr1"] == row["chr2"]:
                    peso *= 2  # Raddoppia il peso se i geni sono sullo stesso cromosoma
                result.append((row["g1"], row["g2"], peso))

            cursor.close()
            cnx.close()
        return result