<script type="text/javascript">
$(function() {
    $("#${w.attrs['id']}").${w.jqmethod}(${w.options});

	% if w.click:
    	$("#${w.attrs['id']}").click(${w.click});
	% endif
});
</script>
