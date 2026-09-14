# kvakk-doc
Public documentation from the Quality in code and coding (KVAKK) group in Statistics Norway.
The content is exported from the Confluence [KVAKK]-pages at Statistics Norway.

The raw export from Confluence is stored in the directory `confluence/raw/`.

## How to export the pages from Confluence?

The export is done by using the open source [confluence-markdown-exporter] (cme) tool.

### Create a Confluence API-token

Create a Confluence API-token with the following scopes:

```
read:confluence-content.all
read:account
read:confluence-content.permission
read:confluence-content.summary
read:confluence-groups
read:confluence-props
read:confluence-space.summary
read:confluence-user
read:me
readonly:content.attachment:confluence
search:confluence
```

### Install and configure the cme tool

```shell
cme config edit auth.confluence

cme config set \
  export.output_path=./confluence/raw \
  export.page_href=relative \
  export.attachment_href=relative \
  export.attachments_export=referenced \
  export.include_document_title=true \
  export.page_breadcrumbs=false \
  export.include_toc=false \
  export.page_properties_format=table \
  export.comments_export=none
```

### Export

Run this command from the root directory of the git-repo:

```shell
cme pages-with-descendants "https://statistics-norway.atlassian.net/wiki/spaces/BEST/pages/3261497397/Kvalitet+i+kode+og+koding"
```


[confluence-markdown-exporter]: https://github.com/Spenhouet/confluence-markdown-exporter
[KVAKK]: https://statistics-norway.atlassian.net/wiki/spaces/BEST/pages/3261497397/Kvalitet+i+kode+og+koding
