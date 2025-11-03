"""
Custom template tags for responsive and optimized image handling.
Provides WebP support with fallbacks for better performance.
"""

from django import template
from django.utils.safestring import mark_safe
import os

register = template.Library()


@register.simple_tag
def webp_picture(image_url, alt_text="", css_class="", lazy=False):
    """
    Generate a <picture> element with WebP and fallback images.

    Usage:
        {% load image_tags %}
        {% webp_picture product.image.url product.name "img-fluid" True %}

    Args:
        image_url: URL of the original image
        alt_text: Alt text for accessibility
        css_class: CSS classes to apply to the img element
        lazy: Whether to apply lazy loading (default: False)

    Returns:
        HTML <picture> element with WebP source and fallback
    """
    if not image_url:
        return ""

    # Convert image URL to WebP
    # Replace file extension with .webp
    base_url, ext = os.path.splitext(image_url)
    webp_url = f"{base_url}.webp"

    # Build lazy loading attribute
    loading_attr = ' loading="lazy"' if lazy else ''

    # Build class attribute
    class_attr = f' class="{css_class}"' if css_class else ''

    # Generate picture element
    html = f'''<picture>
    <source srcset="{webp_url}" type="image/webp">
    <img src="{image_url}" alt="{alt_text}"{class_attr}{loading_attr}>
</picture>'''

    return mark_safe(html)


@register.simple_tag
def webp_img(image_path, media_url, alt_text="", css_class="", style="", lazy=False):
    """
    Generate a <picture> element for images referenced by path (like blog images).

    Usage:
        {% load image_tags %}
        {% webp_img post.image MEDIA_URL post.title "img-fluid" "width: 100%; height: 100%; object-fit:cover;" True %}

    Args:
        image_path: Relative path to the image (e.g., "vinyl-album.jpg")
        media_url: MEDIA_URL from context
        alt_text: Alt text for accessibility
        css_class: CSS classes to apply to the img element
        style: Inline CSS styles
        lazy: Whether to apply lazy loading (default: False)

    Returns:
        HTML <picture> element with WebP source and fallback
    """
    if not image_path:
        return ""

    # Convert ImageFieldFile to string if necessary
    image_path_str = str(image_path)

    # Full image URL
    full_url = f"{media_url}{image_path_str}"

    # Convert to WebP URL
    base_path, ext = os.path.splitext(image_path_str)
    webp_path = f"{base_path}.webp"
    webp_url = f"{media_url}{webp_path}"

    # Build attributes
    loading_attr = ' loading="lazy"' if lazy else ''
    class_attr = f' class="{css_class}"' if css_class else ''
    style_attr = f' style="{style}"' if style else ''

    # Generate picture element
    html = f'''<picture>
    <source srcset="{webp_url}" type="image/webp">
    <img src="{full_url}" alt="{alt_text}"{class_attr}{style_attr}{loading_attr}>
</picture>'''

    return mark_safe(html)
