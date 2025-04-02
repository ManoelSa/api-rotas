from fastapi import HTTPException, APIRouter
from utils.utils import Item, ItemResponse, connect_db

router = APIRouter()

@router.post("/produto/")        #,response_model=ItemResponse)
async def create_produto(item: Item):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        # Inserindo dados na tabela 'produto'
        cursor.execute("INSERT INTO produto (name, description, price) VALUES (?, ?, ?)", 
                       (item.name, item.description, item.price))
        conn.commit()
        conn.close()
        
        return ItemResponse(message="Item criado com sucesso", item=item)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao inserir item: {e}")