// GreenClassify - Main JavaScript File
// Deep Learning Vegetable Classification

document.addEventListener('DOMContentLoaded', function() {
    
    // File Input Handler
    const fileInput = document.getElementById('image');
    const fileName = document.querySelector('.file-name');
    
    if (fileInput && fileName) {
        fileInput.addEventListener('change', function(e) {
            if (this.files && this.files[0]) {
                fileName.textContent = this.files[0].name;
                
                // Preview image (optional)
                const reader = new FileReader();
                reader.onload = function(e) {
                    // Could add image preview here if needed
                    console.log('File loaded successfully');
                };
                reader.readAsDataURL(this.files[0]);
            } else {
                fileName.textContent = 'No file chosen';
            }
        });
    }

    // Smooth Scrolling for Navigation Links
    const navLinks = document.querySelectorAll('a[href^="#"]');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // Navbar Scroll Effect
    const navbar = document.querySelector('.navbar');
    if (navbar) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 50) {
                navbar.style.boxShadow = '0 4px 15px rgba(0, 0, 0, 0.2)';
            } else {
                navbar.style.boxShadow = '0 4px 6px rgba(0, 0, 0, 0.1)';
            }
        });
    }

    // Form Validation
    const uploadForm = document.querySelector('form');
    if (uploadForm) {
        uploadForm.addEventListener('submit', function(e) {
            const imageInput = document.getElementById('image');
            
            if (!imageInput.files || !imageInput.files[0]) {
                e.preventDefault();
                alert('Please select an image file to classify.');
                return false;
            }

            // Check file type
            const allowedTypes = ['image/jpeg', 'image/png', 'image/gif', 'image/webp'];
            const fileType = imageInput.files[0].type;
            
            if (!allowedTypes.includes(fileType)) {
                e.preventDefault();
                alert('Please select a valid image file (JPEG, PNG, GIF, or WEBP).');
                return false;
            }

            // Check file size (max 10MB)
            const maxSize = 10 * 1024 * 1024; // 10MB
            if (imageInput.files[0].size > maxSize) {
                e.preventDefault();
                alert('File size must be less than 10MB.');
                return false;
            }

            // Show loading state
            const submitBtn = uploadForm.querySelector('.submit-btn');
            if (submitBtn) {
                submitBtn.textContent = 'Classifying...';
                submitBtn.disabled = true;
            }
        });
    }

    // Animation on Scroll for Feature Cards
    const featureCards = document.querySelectorAll('.feature-card');
    
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver(function(entries, observer) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    featureCards.forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';
        card.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
        observer.observe(card);
    });

    // Simple Carousel (if needed in the future)
    class Carousel {
        constructor(element) {
            this.carousel = element;
            this.items = element.querySelectorAll('.carousel-item');
            this.currentIndex = 0;
            
            if (this.items.length > 1) {
                this.init();
            }
        }

        init() {
            this.showItem(this.currentIndex);
            setInterval(() => this.next(), 5000);
        }

        showItem(index) {
            this.items.forEach((item, i) => {
                item.style.display = i === index ? 'block' : 'none';
            });
        }

        next() {
            this.currentIndex = (this.currentIndex + 1) % this.items.length;
            this.showItem(this.currentIndex);
        }

        prev() {
            this.currentIndex = (this.currentIndex - 1 + this.items.length) % this.items.length;
            this.showItem(this.currentIndex);
        }
    }

    // Initialize carousel if exists
    const carouselElement = document.querySelector('.carousel');
    if (carouselElement) {
        new Carousel(carouselElement);
    }

    // Console log for debugging
    console.log('GreenClassify JS loaded successfully!');
});

// Utility Functions
const GreenClassify = {
    // Format file size
    formatFileSize: function(bytes) {
        if (bytes === 0) return '0 Bytes';
        const k = 1024;
        const sizes = ['Bytes', 'KB', 'MB', 'GB'];
        const i = Math.floor(Math.log(bytes) / Math.log(k));
        return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
    },

    // Validate image file
    isValidImage: function(file) {
        const validTypes = ['image/jpeg', 'image/png', 'image/gif', 'image/webp'];
        return validTypes.includes(file.type);
    },

    // Show notification
    showNotification: function(message, type = 'info') {
        const notification = document.createElement('div');
        notification.className = `notification notification-${type}`;
        notification.textContent = message;
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            padding: 1rem 2rem;
            background: ${type === 'error' ? '#f44336' : '#4caf50'};
            color: white;
            border-radius: 5px;
            z-index: 9999;
            animation: slideIn 0.3s ease;
        `;
        document.body.appendChild(notification);
        
        setTimeout(() => {
            notification.remove();
        }, 3000);
    }
};
