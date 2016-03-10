from tethys_sdk.base import TethysAppBase, url_map_maker


class TheUnderground(TethysAppBase):
    """
    Tethys app class for The Underground.
    """

    name = 'The Underground'
    index = 'the_underground:home'
    icon = 'the_underground/images/underground-icon.gif'
    package = 'the_underground'
    root_url = 'the-underground'
    color = '#0066ff'
    description = 'This is a map showing common routes and important locations for the Underground Railroad.'
    enable_feedback = False
    feedback_emails = []

        
    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (UrlMap(name='home',
                           url='the-underground',
                           controller='the_underground.controllers.home'),
        )

        return url_maps