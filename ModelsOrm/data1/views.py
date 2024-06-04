from django.views import View
from django.http.response import JsonResponse
from .Authorschema import author_schema, book_schema
from .serializers import AuthorSerializer,BookSerializer
from .models import Author, Books
import jsonschema
import json
from django.utils.timezone import now
import traceback
import logging
logger = logging.getLogger(__file__)

# Create your views here.
class AuthorView(View):

    def get(self, request):
        try:
            all_authors = Author.objects.all()
            authors_serialized = AuthorSerializer(all_authors,many=True,context={"request": request})
            return JsonResponse(authors_serialized.data, safe=False, status=200)
        except Exception as e:
            logger.error(f'ran into error {e}')
            traceback.print_exc()
            return JsonResponse({'success':False},status=400)
    
    def post(self,request):
        try:
            data = json.loads(request.body)
            jsonschema.validate(data,schema=author_schema)
        except (jsonschema.ValidationError,json.decoder.JSONDecodeError) as exc:
            return JsonResponse({"success":False,"message":str(exc)},status=400)
        author = Author(
            name=data.get("name"),
            experience=data.get("experience")
        )
        author.save()
        return JsonResponse({"author id":author.id},status=200)
    
class AuthorExperienceView(View):

    def patch(self,request,id: int):
        try:
            data = json.loads(request.body)
            jsonschema.validate(data,schema=author_schema)
        except (jsonschema.ValidationError,json.decoder.JSONDecodeError) as exc:
            return JsonResponse({"success":False,"message":str(exc)},status=400)
        try:
            author = Author.objects.get(id=id)
            author.experience = data.get("experience")
            author.save()
            return JsonResponse(author.get_author(),status=200)
        except Exception as e:
            logger.error(f'ran into error {e}')
            traceback.print_exc()
            return JsonResponse({'success':False},status=400)
        
    def delete(self,request,id: int):
        try:
            author = Author.objects.get(id=id)
            author.delete()
            return JsonResponse({"success":True},status=200)
        except Exception as e:
            logger.error(f'ran into error {e}')
            traceback.print_exc()
            return JsonResponse({'success':False},status=400)
        
class BookView(View):

    def get(self,request):
        try:
            all_books = Books.objects.all()
            serialized_book = BookSerializer(all_books,many=True,context = {"request": request})
            return JsonResponse(serialized_book.data,safe=False,status = 200)
        except Exception as e:
            logger.error(f'ran into error {e}')
            traceback.print_exc()
            return JsonResponse({'success':False},status=400)

    def post(self, request):
        try:
            data = json.loads(request.body)
            jsonschema.validate(data,schema=book_schema)
        except (jsonschema.ValidationError, json.decoder.JSONDecodeError) as exc:
            return JsonResponse({"success":False,"message":str(exc)},status=400)
        book = Books(
            title=data.get("title"),
            pages=data.get("pages"),
            price=data.get("price")
        )

        author_id = data.get("auth_id")
        author = Author.objects.get(id = author_id)
        book.author = author
        book.save()
        return JsonResponse({"book id":book.id},status=200)
    
class BookManageView(View):

    def getTimeTaken(self,id):
        try:
            book = Books.objects.get(id = id)
            start = book.start_date
            publish = book.published_date
            difference_in_time = publish - start
            days = difference_in_time.days
            book.time_diff = days
            book.save()
            return True
        except Exception as e:
            raise(KeyError)

    def patch(self,request,id: int):
        try:
            data = json.loads(request.body)
            jsonschema.validate(data,schema=book_schema)
        except (jsonschema.ValidationError,json.decoder.JSONDecodeError) as exc:
            return JsonResponse({"success":False,"message":str(exc)},status=400)
        try:
            book = Books.objects.get(id=id)
            data['updated_at']=now()
            for key, value in data.items():
                setattr(book, key, value)
            book.save()
            if 'published_date' in data.keys():
                self.getTimeTaken(id)
            return JsonResponse(book.get_book(),status=200)
        except Exception as e:
            logger.error(f'ran into error {e}')
            traceback.print_exc()
            return JsonResponse({'success':False},status=400)
        
    def delete(self,request,book_id):
        try:
            book = Books.objects.get(id=book_id)
            book.delete()
            return JsonResponse({"success":True},status=200)
        except Exception as e:
            logger.error(f'ran into error {e}')
            traceback.print_exc()
            return JsonResponse({'success':False},status=400)
        
    

