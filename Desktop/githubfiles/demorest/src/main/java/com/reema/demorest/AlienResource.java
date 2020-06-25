package com.reema.demorest;

import javax.ws.rs.GET;
import javax.ws.rs.POST;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

import java.util.List;

@Path("aliens")
public class AlienResource {

	AlienRepository repo=new AlienRepository();
	
	@GET
	@Produces(MediaType.APPLICATION_XML)
	public List<Alien> getAlien()
	{
		System.out.println("get it now");
		
		
		
		return repo.getAliens();
	}
	
	@POST
	@Path("alien")
	public Alien createAlien(Alien a1)
	{
		System.out.println(a1);
		repo.create(a1);
		
		return a1;
	}
}
