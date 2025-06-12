import React, { useState, useEffect } from 'react';
import './App.css';

interface Post {
  id: number;
  title: string;
  content: string;
  created_at: string;
}

function App() {
  const [posts, setPosts] = useState<Post[]>([]);
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');

  const fetchPosts = async () => {
    try {
      const response = await fetch('http://localhost:8000/api/posts');
      const data = await response.json();
      setPosts(data);
    } catch (error) {
      console.error('Error fetching posts:', error);
    }
  };

  const createPost = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!title.trim() || !content.trim()) return;

    try {
      const response = await fetch('http://localhost:8000/api/posts', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ title, content }),
      });
      
      if (response.ok) {
        setTitle('');
        setContent('');
        fetchPosts();
      }
    } catch (error) {
      console.error('Error creating post:', error);
    }
  };

  useEffect(() => {
    fetchPosts();
  }, []);

  return (
    <div className="App">
      <div className="container">
        <h1>간단한 게시판</h1>
        
        <form onSubmit={createPost} className="post-form">
          <h2>새 글 작성</h2>
          <input
            type="text"
            placeholder="제목을 입력하세요"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            className="title-input"
          />
          <textarea
            placeholder="내용을 입력하세요"
            value={content}
            onChange={(e) => setContent(e.target.value)}
            className="content-input"
            rows={4}
          />
          <button type="submit" className="submit-btn">글 작성</button>
        </form>

        <div className="posts-section">
          <h2>게시글 목록</h2>
          {posts.length === 0 ? (
            <p className="no-posts">아직 작성된 글이 없습니다.</p>
          ) : (
            <div className="posts-list">
              {posts.map((post) => (
                <div key={post.id} className="post-item">
                  <h3 className="post-title">{post.title}</h3>
                  <p className="post-content">{post.content}</p>
                  <small className="post-date">{post.created_at}</small>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
