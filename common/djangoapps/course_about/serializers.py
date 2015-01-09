"""
Serializers for all Course Descriptor and Course About Descriptor related return objects.

"""
from util.parsing_utils import course_image_url


def serialize_content(course_descriptor, about_descriptor):
    """
    Returns a serialized representation of the course_descriptor and about_descriptor
    Args:
        course_descriptor(CourseDescriptor) : course descriptor object
        about_descriptor(dict) : Dictionary of CourseAboutDescriptor objects
    return:
        serialize data for course information.
    """
    data = {
        'media': {},
        'display_name': getattr(course_descriptor, 'display_name', None),
        'course_number': course_descriptor.location.course,
        'course_id': None,
        'advertised_start': getattr(course_descriptor, 'advertised_start', None),
        'is_new': getattr(course_descriptor, 'is_new', None),
        'start': None,
        'end': None,
        'announcement': None,
        'effort': about_descriptor.get("effort", None)

    }

    content_id = unicode(course_descriptor.id)
    data["course_id"] = unicode(content_id)
    if getattr(course_descriptor, 'course_image', False):
        data['media']['image'] = course_image_url(course_descriptor)

    start = getattr(course_descriptor, 'start', None)
    end = getattr(course_descriptor, 'end', None)
    announcement = getattr(course_descriptor, 'announcement', None)

    data['start'] = start.strftime('%Y-%m-%d') if start else None
    data['end'] = end.strftime('%Y-%m-%d') if end else None
    data["announcement"] = announcement.strftime('%Y-%m-%d') if announcement else None

    return data

