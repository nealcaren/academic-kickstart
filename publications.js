/**
 * Publications Page Interactions
 * - Copy citation functionality
 * - Smooth scroll for expanded abstracts
 */

document.addEventListener('DOMContentLoaded', function() {
  // Copy citation functionality
  const copyButtons = document.querySelectorAll('.btn-copy-citation');

  copyButtons.forEach(button => {
    button.addEventListener('click', async function() {
      const citation = this.getAttribute('data-citation');

      try {
        // Use Clipboard API
        await navigator.clipboard.writeText(citation);

        // Visual feedback
        const originalHTML = this.innerHTML;
        this.innerHTML = '<i class="bi bi-check2"></i> Copied!';
        this.classList.add('copied');

        // Reset after 2 seconds
        setTimeout(() => {
          this.innerHTML = originalHTML;
          this.classList.remove('copied');
        }, 2000);

      } catch (err) {
        console.error('Failed to copy citation:', err);

        // Fallback for older browsers
        const textArea = document.createElement('textarea');
        textArea.value = citation;
        textArea.style.position = 'fixed';
        textArea.style.left = '-999999px';
        document.body.appendChild(textArea);
        textArea.select();

        try {
          document.execCommand('copy');
          const originalHTML = this.innerHTML;
          this.innerHTML = '<i class="bi bi-check2"></i> Copied!';
          this.classList.add('copied');
          setTimeout(() => {
            this.innerHTML = originalHTML;
            this.classList.remove('copied');
          }, 2000);
        } catch (fallbackErr) {
          console.error('Fallback copy failed:', fallbackErr);
        }

        document.body.removeChild(textArea);
      }
    });
  });

  // Smooth scroll when abstract is opened
  const abstracts = document.querySelectorAll('.publication-abstract');

  abstracts.forEach(abstract => {
    abstract.addEventListener('toggle', function() {
      if (this.open) {
        setTimeout(() => {
          this.scrollIntoView({
            behavior: 'smooth',
            block: 'nearest'
          });
        }, 100);
      }
    });
  });
});
