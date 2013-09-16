from parsley.decorators import parsleyfy

class ParsleyMixin(object):

    def get_form(self, *args, **kwargs):
        form = super(ParsleyMixin, self).get_form(*args, **kwargs)
        return parsleyfy(form)
