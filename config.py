config.register_asset(
    'main_css',
    'reset.css',
    'main.css',
    'pygment.css',
    output="cache_main.%(version)s.css")

config.context_update(
    name="dlangdive",
    url="http://dlangdive.org",
    fb_app_id="641472525895652",
)
