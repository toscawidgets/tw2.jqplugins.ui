<script type="text/javascript">
$(function() {
    $("#${w.attrs['sel']}").${w.jqmethod}(${w.options});
	% if w.click:
    	$("#${w.attrs['sel']}").click(${w.click});
	% endif
});
</script>
