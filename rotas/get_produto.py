from fastapi import HTTPException, APIRouter
from utils.utils import connect_db

router = APIRouter()

@router.get("/produto/")
async def get_produto():
    try:
        conn = connect_db()
        cursor = conn.cursor()

        # Selecionando todos os itens da tabela 'produto'
        cursor.execute("SELECT * FROM produto")
        itens = cursor.fetchall()
        conn.close()
        
        return [{"id": row[0],
                  "name": row[1],
                  "description": row[2],
                  "price": row[3]
                } for row in itens]

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro na leitura: {e}")