## Docker for Mac download links

Release versions can be correlated against the
[Official Release Notes](https://docs.docker.com/docker-for-mac/release-notes/).

Note: Not all builds result in a release, so it's recommended you pick the
largest build number for the particular release you're interested in.

## Stable

{% assign stable_versions = site.data.stable | group_by: 'x-amz-meta-version' %}
{% for version in stable_versions %}
### {{ version.name }}

{% assign builds = (version.items | sort: 'x-ams-meta-build') | reverse -%}
{% for build in builds -%}
* [Build {{ build.x-amz-meta-build }}]({{ build.url }})
{% endfor %}
{% endfor %}

## Edge

{% assign edge_versions = site.data.edge | group_by: 'x-amz-meta-version' %}
{% for version in edge_versions %}
### {{ version.name }}

{% assign builds = (version.items | sort: 'x-ams-meta-build') | reverse -%}
{% for build in builds -%}
* [Build {{ build.x-amz-meta-build }}]({{ build.url }})
{% endfor %}
{% endfor %}
