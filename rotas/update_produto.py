from fastapi import HTTPException, APIRouter
from utils.utils import Item, ItemResponse, connect_db

router = APIRouter()

@router.put("/produto/{id}")
async def update_produto(id:int, produto:Item):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        # Atualizando um produto da tabela de acordo com o ID e Parametros recebido
        cursor.execute("UPDATE produto SET name = ?, description = ?, price = ? WHERE id = ?",
                        (produto.name, produto.description, produto.price, id)
                       )

        conn.commit()
        conn.close()
        return ItemResponse(message="Item Atualizado com sucesso", item=produto)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro na Atualização: {e}")