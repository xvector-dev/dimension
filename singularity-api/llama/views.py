from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.http import HttpResponse
from rest_framework.permissions import AllowAny, IsAuthenticated
from .llama_handler import HandleLLamaModel
import json
from conversation.views import save_conversation
from code_assistant.views import save_code_conversation
from sales_assistant.views import save_sales_conversation
from youtube_assistant.views import save_youtube_conversation


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def conversational(request, *args, **kwargs):
    data = request.data
    prompt = data['prompt']
    task = data['task']
    slug = data['slug'] if 'slug' in data else None
    context = data['context'] if 'context' in data else ''
    should_save_conversation = data['save_conversation'] if 'save_conversation' in data else False

    llama = HandleLLamaModel(task=task)
    response = llama.generate_response(prompt=prompt, context=context)

    if should_save_conversation:
        uuid_slug = save_conversation(
            user=request.user, conversation_uuid=slug, prompt=prompt, conversation_dict=response)
        response['slug'] = uuid_slug

    return HttpResponse(json.dumps(response), status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def code_generation(request, *args, **kwargs):
    data = request.data
    prompt = data['prompt']
    task = data['task']
    context = data['context'] if 'context' in data else ''
    slug = data['slug'] if 'slug' in data else None
    should_save_conversation = data['save_conversation'] if 'save_conversation' in data else False

    llama = HandleLLamaModel(task=task)
    response = llama.generate_response(prompt=prompt, context=context)

    print(response)

    if should_save_conversation:
        uuid_slug = save_code_conversation(
            user=request.user, conversation_uuid=slug, prompt=prompt, conversation_dict=response)
        response['slug'] = uuid_slug

    return HttpResponse(json.dumps(response), status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def seo_generation(request, *args, **kwargs):
    data = request.data
    prompt = data['prompt']
    task = data['task']
    context = data['context'] if 'context' in data else ''
    slug = data['slug'] if 'slug' in data else None
    should_save_conversation = data['save_conversation'] if 'save_conversation' in data else False

    llama = HandleLLamaModel(task=task)
    response = llama.generate_response(prompt=prompt, context=context)

    if should_save_conversation:
        uuid_slug = save_youtube_conversation(
            user=request.user, conversation_uuid=slug, prompt=prompt, conversation_dict=response)
        response['slug'] = uuid_slug

    return HttpResponse(json.dumps(response), status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def sales(request, *args, **kwargs):
    data = request.data
    prompt = data['prompt']
    task = data['task']
    context = data['context'] if 'context' in data else ''
    slug = data['slug'] if 'slug' in data else None
    should_save_conversation = data['save_conversation'] if 'save_conversation' in data else False

    llama = HandleLLamaModel(task=task)
    response = llama.generate_response(prompt=prompt, context=context)

    if should_save_conversation:
        uuid_slug = save_sales_conversation(
            user=request.user, conversation_uuid=slug, prompt=prompt, conversation_dict=response)
        response['slug'] = uuid_slug

    return HttpResponse(json.dumps(response), status=status.HTTP_200_OK)
