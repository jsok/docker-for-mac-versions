## Docker for Mac download links

## Stable

{% for build in site.data.stable %}
* [{{ build.x-amz-meta-version }} Build {{ build.x-amz-meta-build }}]({{ build.url }})
{% endfor %}

## Edge

{% for build in site.data.edge %}
* [{{ build.x-amz-meta-version }} Build {{ build.x-amz-meta-build }}]({{ build.url }})
{% endfor %}
