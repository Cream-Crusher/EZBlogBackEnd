from typing import List

from fastapi import APIRouter, Depends, HTTPException

from api.comment.schema import CommentCreate
from api.comment.schema import CommentRead, CommentUpdate
from api.comment.service import comment_service
from utils.Auth.authentication import get_me
from utils.base.pagination import Pagination

router = APIRouter(prefix='/comment', tags=['Comment|Comments'])


@router.get('/', name='Get All Comment', response_model=List[CommentRead])
async def get_all_comments(comments=comment_service, paging=Depends(Pagination)):
    return await comments.all(paging)


@router.get('/{comment_id}', name='Get Comment By Id', response_model=CommentRead)
async def comment_by_id(comment_id: str, comments=comment_service, me=Depends(get_me)):
    return await comments.id(comment_id)


@router.post('/', name='Create Comment', status_code=201)
async def create_comment(comment: CommentCreate, comments=comment_service, me=Depends(get_me)):
    if me.role not in ["admin", "user"]:
        raise HTTPException(403, "forbidden")

    return await comments.create(comment.__dict__)


@router.delete('/{comment_id}', name='Delete Comment By Id')
async def del_comment(comment_id: str, comments=comment_service, me=Depends(get_me)):
    comment_author_id = (await comments.id(comment_id)).author_id

    if not (me.role in ["admin"] or comment_author_id == me.id):
        raise HTTPException(403, "forbidden")

    return await comments.delete(comment_id)


@router.patch('/', name='Update Comment By Id', response_model=CommentRead)
async def update_comment(comment_id: str, comment: CommentUpdate, comments=comment_service, me=Depends(get_me)):
    comment_author_id = (await comments.id(comment_id)).author_id

    if not (me.role in ["admin"] or comment_author_id == me.id):
        raise HTTPException(403, "forbidden")

    return await comments.update(comment_id, comment.__dict__)
