## Docker for Mac download links

## Stable

{% assign stable = (site.data.stable | sort: 'x-amz-meta-build' ) | reverse %}
{% for build in stable %}
* [{{ build.x-amz-meta-version }} Build {{ build.x-amz-meta-build }}]({{ build.url }})
{% endfor %}

## Edge

{% assign edge = (site.data.edge | sort: 'x-amz-meta-build' ) | reverse %}
{% for build in edge %}
* [{{ build.x-amz-meta-version }} Build {{ build.x-amz-meta-build }}]({{ build.url }})
{% endfor %}
