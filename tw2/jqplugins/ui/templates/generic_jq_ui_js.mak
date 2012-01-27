<script type="text/javascript">
$(document).ready(function() {
    $("#${w.selector}").${w.jqmethod}(${w.options});
	% if w.events:
	% for k in w.events:
    	$("#${w.selector}").bind("${k}", ${w.events[k]});
	% endfor
	% endif
});
</script>
