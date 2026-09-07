from fastapi import APIRouter

router =APIRouter() 

@router.get("/pagamentos")
def buscar_pagamentos():
    return{"mensagem":"Rota busca de pagamentos funcionando"}