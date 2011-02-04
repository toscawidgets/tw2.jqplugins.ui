<script type="text/javascript">
$(function() {
    $("#${w.selector}").${w.jqmethod}(${w.options});
	% if w.click:
    	$("#${w.selector}").click(${w.click});
	% endif
});
</script>
