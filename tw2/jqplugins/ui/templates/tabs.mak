<%namespace name="tw" module="tw2.core.mako_util"/>
<div id="${w.attrs['id']}:wrapper">
<div ${tw.attrs(attrs=w.attrs)}>
    <ul>
    % for i in range(len(w.items)):
        <li><a href="${w.items[i].get('href','#'+ w.attrs['id']+':'+str(i))}">
            ${w.items[i].get('label', '(no label)')}
        </a></li>
    % endfor
    </ul>
    % for i in range(len(w.items)):
        % if 'content' in w.items[i]:
    <div id="${w.attrs['id']}:${str(i)}">
        ${w.items[i]['content']}
    </div>
        % endif
    % endfor
</div>
<%include file="generic_jq_ui_js.mak" />
</div>
