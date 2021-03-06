import logging
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from annotations.models import Annotation
from recordings.models import Recording

#
# Views
#
def index(request):
    annotations = Annotation.objects.all()
    return render_to_response('annotations/index.html', {'annotations' : annotations})

def show(request, annotation_id):
    annotation = get_object_or_404(Annotation,pk=annotation_id)
    return render_to_response('annotations/show.html', {'annotation' : annotation})

def update(request):
    """
    Update the database with new annotations from the AudioAnnotator Flash interface.

    The Flash interface will output a string that looks like:

    "1,62637,119960,test\n2,137802,175384,test2\n"

    Each new line is a new annotation.  The first field is the
    annotation id, the second and third are the start and end times,
    in milliseconds, and the fourth is the label.
    """
    
    if request.method == "POST":
        annotations = request.POST.get('annotations', '')
        recording = Recording.objects.get(pk=request.POST.get('recording_id', ''))

        # Take the string of annotations from the AudioAnnotator and
        # parse it into annotations.
        for annotation in annotations.split("\n"):
            if (annotation == ''):
                break
            fields = annotation.split(",")
            ann_id = fields[0]
            ann_start_ms = int(fields[1])
            ann_end_ms = int(fields[2])
            ann_label = fields[3]
            # if (ann_label == None):
            #     Annotation.delete(ann_id)
            #     break

            if (ann_id == "0"):
                ann = Annotation(
                    start_time_ms = ann_start_ms,
                    end_time_ms = ann_end_ms,
                    label = ann_label,
                    recording = recording)
                ann.save()
            else:
                ann = Annotation.objects.get(pk=ann_id)
                ann.start_time_ms = ann_start_ms
                ann.end_time_ms = ann_end_ms
                ann.label = ann_label
                print ann
                ann.save()


    # Return back to the AudioAnnotator the latest collection of
    # annotations for this recording.
    annotations = Annotation.objects.all().filter(recording=r)
    output = ""
    for annotation in annotations:
        output += annotation.to_string + "\n"

    logging.info("***output=" + output)
    return HttpResponse(output)
    

