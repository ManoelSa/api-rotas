from fastapi import HTTPException, APIRouter
from utils.utils import ItemResponse, connect_db

router = APIRouter()

@router.delete("/produto/{id}")
async def delete_produto(id:int):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        # Deletando um produto da tabela de acordo com o ID recebido'
        cursor.execute("DELETE FROM produto WHERE id = ?",(id,))

        conn.commit()
        conn.close()
        
        return {"message": "Produto DELETADO com sucesso!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro na Deleção: {e}")