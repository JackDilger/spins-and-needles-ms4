"""
Custom middleware for adding security headers.
"""


class SecurityHeadersMiddleware:
    """
    Adds additional security headers to all responses.

    Headers added:
    - Cross-Origin-Opener-Policy: same-origin (COOP)
    - Content-Security-Policy: Restricts resource loading for XSS protection
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Add COOP header - isolates the browsing context
        response['Cross-Origin-Opener-Policy'] = 'same-origin'

        # Add CSP header - restrict resource loading
        # Policy breakdown:
        # - default-src 'self': Only load resources from same origin by default
        # - script-src: Allow scripts from self, Stripe, jQuery CDN, FontAwesome, and inline scripts (needed for Stripe)
        # - style-src: Allow styles from self, Bootstrap CDN, FontAwesome, and inline styles (needed for Bootstrap)
        # - img-src: Allow images from self, S3 bucket, Stripe, and data URIs
        # - font-src: Allow fonts from self, FontAwesome CDN
        # - connect-src: Allow API connections to self and Stripe
        # - frame-src: Allow iframes from Stripe (for 3D Secure)
        csp_policy = (
            "default-src 'self'; "
            "script-src 'self' 'unsafe-inline' https://js.stripe.com https://code.jquery.com https://cdn.jsdelivr.net https://kit.fontawesome.com; "
            "style-src 'self' 'unsafe-inline' https://stackpath.bootstrapcdn.com https://ka-f.fontawesome.com; "
            "img-src 'self' https://spins-and-needles.s3.amazonaws.com https://spins-and-needles.s3.eu-west-2.amazonaws.com https://*.stripe.com data:; "
            "font-src 'self' https://ka-f.fontawesome.com; "
            "connect-src 'self' https://api.stripe.com https://ka-f.fontawesome.com; "
            "frame-src https://js.stripe.com; "
            "object-src 'none'; "
            "base-uri 'self'; "
            "form-action 'self';"
        )
        response['Content-Security-Policy'] = csp_policy

        return response
