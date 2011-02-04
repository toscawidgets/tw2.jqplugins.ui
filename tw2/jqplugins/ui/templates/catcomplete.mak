<%namespace name="tw" module="tw2.core.mako_util"/>
<div id="${w.attrs['id']}:wrapper">
    <style>
    .ui-autocomplete-category {
        font-weight: bold;
        padding: .6em .12em;
        margin: .8em 0 .2em;
        line-height: 1.5;
    }
    </style>
    <input ${tw.attrs(attrs=w.attrs)} />
<%include file="generic_jq_ui_js.mak" />
% if w.attrs['value'] != '':
	<%include file="ghost_text.mak" />
% endif
</div>
