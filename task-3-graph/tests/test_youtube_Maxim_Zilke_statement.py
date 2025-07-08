import pytest
from streamlink.plugins.youtube import YouTube





def test_normal_stream_quality():
        """Test normal stream quality like 720p, 1080p"""
        weight, group = YouTube.stream_weight("720p")
        assert isinstance(weight, int)
        assert group == "pixels"  # Plugin.stream_weight returns "pixels" for quality formats
        # testet, dass man einen normalen Stream hat else fall ausgeführt wird  
    

    
def test_3d_stream_reduces_weight():
         """Test that 3D streams get reduced weight and special group"""
         weight_normal, group_normal = YouTube.stream_weight("720p")
         weight_3d, group_3d = YouTube.stream_weight("720p_3d")
        
         assert weight_3d == weight_normal - 1
         assert group_3d == "youtube_3d"
        # testet den if fall
         
    
def test_high_frame_rate_increases_weight():
         """Test that HFR streams get increased weight and special group"""
         weight_normal, group_normal = YouTube.stream_weight("720p")
         weight_hfr, group_hfr = YouTube.stream_weight("720p60")
          
         assert weight_hfr == weight_normal + 1
         assert group_hfr == "high_frame_rate"
         #testet den elif fall
    

