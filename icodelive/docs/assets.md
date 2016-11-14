<link href="//maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet">
<script>
    (function($){
        var $span = $('<span class="fa" style="display:none"></span>').appendTo('body');
        if ($span.css('fontFamily') !== 'FontAwesome' ) {
            // Fallback Link
            $('head').append('<link href="/css/font-awesome.min.css" rel="stylesheet">');
        }
        $span.remove();
    })(jQuery);
</script>

