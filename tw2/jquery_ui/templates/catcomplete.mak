<div xmlns:py="http://genshi.edgewall.org/"
     xmlns:xi="http://www.w3.org/2001/XInclude"
     id="${w.attrs['id']}-wrapper">

    <style> 
    .ui-autocomplete-category {
        font-weight: bold;
        padding: .6em .12em;
        margin: .8em 0 .2em;
        line-height: 1.5;
    }
    </style> 

     <input py:attrs="w.attrs"/>
<xi:include href="generic_jq_ui_js.html" />
<xi:include href="ghost_text.html" py:if="w.attrs['value']!=''" />
</div>
